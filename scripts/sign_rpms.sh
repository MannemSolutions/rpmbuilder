#!/bin/bash
set -e

[ ! -d /host/secrets ] && exit 0

[ -e /host ] && DEST=/host || DEST=/tmp
export RPMDEST=${RPMDEST:-${DEST}/rpms}

cp /host/secrets/.rpmmacros ~/
cat /host/gpg_pubkey.asc | gpg --import --no-tty --batch --yes
cat /host/secrets/GPG_KEY | base64 -d | gpg --import --no-tty --batch --yes
rpmsign --addsign "${RPMDEST}/"*.rpm

echo Siging finished succesfully
