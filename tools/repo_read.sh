#!/bin/bash
# Read-only access to herrrickshaw repos for Track D, as one fixed command so an unattended run needs
# exactly one permission rule: Bash(bash /Users/Shared/lit_review/tools/repo_read.sh *)
# Usage:
#   repo_read.sh tree <repo>                 list every file path in the default branch
#   repo_read.sh file <repo> <path>          print one file
#   repo_read.sh grep <repo> <regex> [glob]  grep the repo's files (shallow, blob-filtered clone, deleted after)
#   repo_read.sh localgrep <regex> <path> [glob]   grep local files, only under the task's three folders:
#                                            ~/market-pipeline, ~/masaladeutsch-archive, /Users/Shared/lit_review
#   repo_read.sh ls <dir>                    list a local folder under those three roots
# Only GET requests, clones and local reads; nothing is ever written anywhere.
set -u
die() { echo "repo_read: $*" >&2; exit 2; }
[ $# -ge 2 ] || die "usage: tree|file|grep <repo> ... | localgrep <regex> <path> [glob] | ls <dir>"
cmd=$1
# Paths are resolved whole (directories via cd + pwd -P, files via realpath), so a trailing "..",
# a symlinked directory or a symlinked file cannot name something outside the roots.
inroots() { local r
  if [ -d "$1" ]; then r=$(cd "$1" 2>/dev/null && pwd -P) || return 1
  else r=$(realpath "$1" 2>/dev/null) || return 1; fi   # files too: a symlinked file must not point outside
  case $r in "$HOME"/market-pipeline/*|"$HOME"/market-pipeline|"$HOME"/masaladeutsch-archive/*|"$HOME"/masaladeutsch-archive|/Users/Shared/lit_review/*|/Users/Shared/lit_review) return 0;; esac; return 1; }
if [ "$cmd" = localgrep ]; then
  [ $# -ge 3 ] || die "usage: localgrep <regex> <path> [glob]"
  inroots "$3" || die "path outside the allowed folders"
  grep -rnE --exclude-dir=.git --exclude-dir=.venv --exclude-dir=node_modules ${4:+--include="$4"} -- "$2" "$3" | head -300
  exit 0
fi
if [ "$cmd" = ls ]; then
  inroots "$2" || die "path outside the allowed folders"
  ls -la "$2"; exit 0
fi
repo=$2
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
