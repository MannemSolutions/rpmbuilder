#!/bin/bash
set -e

cd $(dirname $0)
./generate_specs.sh
./build_rpms.sh
./sign_rpms.sh

echo Done
