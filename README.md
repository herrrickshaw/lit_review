# lit_review

Collected output of the `literature-review-daily` scheduled task, kept in one place so
the review record is versioned independently of the two repos it reads from.

This repo is a **mirror of review artifacts only**. The source-of-truth copies live in
their own repos, and the scheduled task writes there, not here:

| here | source of truth |
|---|---|
| `market-pipeline/LITERATURE_REGISTER.md` | `~/market-pipeline/research/LITERATURE_REGISTER.md` |
| `market-pipeline/BACKTEST_QUEUE.md` | `~/market-pipeline/research/BACKTEST_QUEUE.md` |
| `market-pipeline/literature_runs/` | `~/market-pipeline/research/literature_runs/` |
| `masaladeutsch/SOURCE_REGISTER.md` | `~/masaladeutsch-archive/docs/SOURCE_REGISTER.md` |
| `masaladeutsch/COMMISSION_QUEUE.md` | `~/masaladeutsch-archive/docs/COMMISSION_QUEUE.md` |
| `masaladeutsch/LITERATURE_SURVEY.md` | `~/masaladeutsch-archive/docs/LITERATURE_SURVEY.md` |
| `task/literature-review-daily.SKILL.md` | `~/.claude/scheduled-tasks/literature-review-daily/SKILL.md` |

`task/` holds the scheduled task's own definition. It is mirrored here because
`~/.claude/` is gitignored in the `$HOME` repo (`.gitignore:49`) — deliberately, and that
repo is public — so this is the only version history the task instructions have. Track C
of the task keeps it current; it is never force-added into the `$HOME` repo.

## The two tracks

**Track A — market-pipeline.** Grades papers on whether a technique is worth
implementing in the daily EOD multi-market equity screener. Bar: risk-adjusted metric
(Sharpe/return/IR) over bare price-level MAPE/RMSE, transaction costs modelled or at
least addressed, disclosed universe and date range. Actionable gaps land in
`BACKTEST_QUEUE.md`; nothing in that file is ever executed automatically.

**Track B — masaladeutsch.** Grades sources on whether they can carry an article:
obtainable primary data, a quantified finding a reader would not already assume, and a
subject the blog has not covered. Vendor market-sizing is WEAK by default. Output is
reading material for a human — never a draft, never a published post.

The two tracks share nothing but the schedule: different repos, different registers,
different bars. A source can pass one and fail the other.

## Conventions worth keeping

- **No fabrication.** Every claim about a paper comes from a page actually fetched;
  every "the repo already does this" comes from a real grep, cited as `file:line`.
- **Grade before reading deeply.** Papers whose headline metric is price-level
  MAPE/RMSE with no cost discussion and an undisclosed universe get one line in the
  weak section, not a write-up.
- **Sparse and honest beats full and padded.** An empty day is a legitimate result and
  is recorded as one.
