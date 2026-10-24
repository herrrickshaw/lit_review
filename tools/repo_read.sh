#!/bin/bash
# Read-only access to herrrickshaw repos for Track D, as one fixed command so an unattended run needs
# exactly one permission rule: Bash(bash /Users/Shared/lit_review/tools/repo_read.sh *)
# Usage:
#   repo_read.sh tree <repo>                 list every file path in the default branch
#   repo_read.sh file <repo> <path>          print one file
#   repo_read.sh grep <repo> <regex> [glob]  grep the repo's files (shallow, blob-filtered clone, deleted after)
# Only GET requests and clones; nothing is ever written to GitHub.
set -u
die() { echo "repo_read: $*" >&2; exit 2; }
[ $# -ge 2 ] || die "usage: tree|file|grep <repo> ..."
cmd=$1; repo=$2
[[ $repo =~ ^[A-Za-z0-9._-]+$ ]] || die "bad repo name"
case $repo in personal-profile|working-files) die "$repo is personal and off-limits";; esac
case $cmd in
  tree)
    gh api "repos/herrrickshaw/$repo/git/trees/HEAD?recursive=1" --jq '.tree[] | select(.type=="blob") | .path' ;;
  file)
    [ $# -eq 3 ] || die "usage: file <repo> <path>"
    [[ $3 =~ ^[A-Za-z0-9._/@+-]+$ && $3 != *..* ]] || die "bad path"
    gh api -H "Accept: application/vnd.github.raw" "repos/herrrickshaw/$repo/contents/$3" ;;
  grep)
    [ $# -ge 3 ] || die "usage: grep <repo> <regex> [glob]"
    d=$(mktemp -d) || exit 1
    trap 'rm -rf "$d"' EXIT
    git clone -q --depth 1 --filter=blob:none "https://github.com/herrrickshaw/$repo.git" "$d/r" 2>/dev/null || die "clone failed"
    grep -rnE --exclude-dir=.git ${4:+--include="$4"} -- "$3" "$d/r" | sed "s#^$d/r/##" | head -200 ;;
  *) die "unknown command $cmd" ;;
esac
