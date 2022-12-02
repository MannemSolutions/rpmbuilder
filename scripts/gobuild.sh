#!/bin/bash
set -e

export PATH=$PATH:/usr/local/go/bin

function usage()
{
  echo $0 $1
  cat << EOF
  usage: $0 [options]...

  This script is used to download and build a golang tool from github.

  OPTIONS:
     -h show this help
     -s site to clone form (usually github.com
     -o organization to clone from (defaults to REPOSITORY)
     -r repository to clone (usually this is the nam the software, like pgquartz, stolon, etc.)
     -t build target(s) supply muliple times for multiple targets
     -x debug option

     Other options are invalid

EOF
  exit ${1:-0}
}

arrTARGETS=()

while [ -n "$1" ]; do
  case $1 in
    -h) usage; exit 0 ;;
    -s) export SITE="$2" ; shift 2 ;;
    -o) export ORGANIZATION="$2" ; shift 2 ;;
    -r) export REPOSITORY="$2" ; shift 2 ;;
    -t) arrTARGETS+=("$2") ; echo "${arrTARGETS[@]}"; shift 2 ;;
    -x) set -x; shift 1 ;;
    *)  echo "error: no such option $1. Issue '$0 -h' for valid options" ; usage 1 ;;
  esac
done
[ "${#arrTARGETS[@]}" -gt 0 ] || arrTARGETS=("build")

if [ -z "${REPOSITORY}" ]; then
  echo "You must set a repository with the -r option"
  usage 1
fi
export SITE=${SITE:-github.com}
export ORGANIZATION=${ORGANIZATION:-${REPOSITORY}}
URL="https://${SITE}/${ORGANIZATION}/${REPOSITORY}.git"

[ ! -e "${REPOSITORY}" ] && git clone "$URL"
cd "${REPOSITORY}"
git fetch
LATEST_COMMIT=${1:-$(git tag | sed '/-/!{s/$/_/}' | sort -V | sed 's/_$//' | tail -n1)}
git checkout "${LATEST_COMMIT}"
go get -v -t -d ./... || echo go get failed

for T in "${arrTARGETS[@]}"; do
  make "${T}"
done
