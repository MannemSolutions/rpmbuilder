#!/bin/bash
set -ex
GOVER=${GOVER:-1.19.3}

PKGARCH=$(uname -m | sed 's/aarch64/arm64/;s/x86_64/amd64/')
cd $(mktemp -d)
curl -L "https://go.dev/dl/go${GOVER}.linux-${PKGARCH}.tar.gz" -o "go${GOVER}.linux-${PKGARCH}.tar.gz"
file "go${GOVER}.linux-${PKGARCH}.tar.gz"
rm -rf /usr/local/go
tar -C /usr/local -xzf go${GOVER}.linux-${PKGARCH}.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> /etc/bashrc
