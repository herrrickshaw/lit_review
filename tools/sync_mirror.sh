#!/bin/bash
# Track C of literature-review-daily as one fixed command, so an unattended run needs exactly one
# permission rule: Bash(bash /Users/Shared/lit_review/tools/sync_mirror.sh *)
# Usage: sync_mirror.sh [--prose-ok] "<commit subject>"   Prints one summary line for the day's log.
# --prose-ok: pass ONLY after reading the secret-scan hits a previous call printed and confirming every one is
# prose (e.g. a post slug containing "token"). Never force-pushes.
set -u
M=/Users/Shared/lit_review
PROSE_OK=0
if [ "${1:-}" = "--prose-ok" ]; then PROSE_OK=1; shift; fi
SUBJECT=${1:-"Sync literature review — $(date +%Y-%m-%d)"}
g() { git -C "$M" "$@"; }

# 1. copy sources -> mirror (portfolio/ is written in place by Track D and is never copied over)
mkdir -p "$M/market-pipeline/literature_runs" "$M/masaladeutsch" "$M/task"
cp ~/market-pipeline/research/LITERATURE_REGISTER.md ~/market-pipeline/research/BACKTEST_QUEUE.md "$M/market-pipeline/" || { echo "SYNC FAILED: copy market-pipeline registers"; exit 0; }
cp ~/market-pipeline/research/literature_runs/*.md "$M/market-pipeline/literature_runs/" || { echo "SYNC FAILED: copy literature_runs"; exit 0; }
cp ~/masaladeutsch-archive/docs/SOURCE_REGISTER.md ~/masaladeutsch-archive/docs/COMMISSION_QUEUE.md ~/masaladeutsch-archive/docs/LITERATURE_SURVEY.md "$M/masaladeutsch/" || { echo "SYNC FAILED: copy masaladeutsch docs"; exit 0; }
cp ~/.claude/scheduled-tasks/literature-review-daily/SKILL.md "$M/task/literature-review-daily.SKILL.md" || { echo "SYNC FAILED: copy task spec"; exit 0; }

# 2. anything to do?
if [ -z "$(g status --porcelain)" ]; then echo "SYNC: no changes, nothing committed"; exit 0; fi

# 3. secret scan of the lines ADDED today in .md files (task/ excluded: it holds this pattern verbatim).
#    Any hit -> unstage, print the hits, stop; re-run with --prose-ok only after reading every hit.
g add -A || { echo "SYNC FAILED: git add"; exit 0; }
HITS=$(g diff --cached -U0 -- '*.md' ':(exclude)task/**' | grep -E '^\+' | grep -v '^+++' \
       | grep -niE 'api[_-]?key|secret|password|passwd|token|bearer|BEGIN [A-Z ]*PRIVATE KEY|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-|AIza[0-9A-Za-z_-]{35}')
if [ -n "$HITS" ] && [ $PROSE_OK -eq 0 ]; then
  g reset -q
  echo "SYNC STOPPED: $(echo "$HITS" | wc -l | tr -d ' ') secret-scan hit(s) in today's added lines. Read each; if every one is prose, re-run with --prose-ok:"
  echo "$HITS" | cut -c1-220 | head -20
  exit 0
fi

# 4. commit and push; on a non-fast-forward rejection, rebase the unpushed commits once and retry
g commit -q -m "$SUBJECT" || { echo "SYNC FAILED: commit"; exit 0; }
SHA=$(g rev-parse --short HEAD)
if g push -q 2>/dev/null; then echo "SYNC: pushed $SHA"; exit 0; fi
if g pull -q --rebase 2>/dev/null && g push -q 2>/dev/null; then
  echo "SYNC: pushed $(g rev-parse --short HEAD) after rebasing onto newer remote commits"; exit 0
fi
g rebase --abort 2>/dev/null
echo "SYNC FAILED: committed $SHA locally, push rejected and rebase did not apply cleanly — needs a human"
exit 0
