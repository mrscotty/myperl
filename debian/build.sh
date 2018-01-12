#!/bin/bash

echo "INFO: HOME=$HOME"
echo "INFO: pwd"
pwd
echo "INFO: ls -latr"
ls -latr

make debian
make debian-install
(cd ex/libdbd-mysql-myperl && make package)
(cd ex/openxpki-core-deps-myperl && make package)

echo "INFO: find / -name \*.deb"
find / -name \*.deb
