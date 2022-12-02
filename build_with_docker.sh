#!/bin/bash
set -e
[ "${#PLATFORMS[@]}" -gt 0 ] || PLATFORMS=('arm64' 'amd64')

for PLATFORM in "${PLATFORMS[@]}"; do
  echo "Building ${PLATFORM}"
  docker build --platform "linux/${PLATFORM}" -t "rpmb_${PLATFORM}" .
  docker run -ti --platform "linux/${PLATFORM}" --name "rpmb_${PLATFORM}" --rm -v "${PWD}:/host"  "rpmb_${PLATFORM}" /start.sh
done
