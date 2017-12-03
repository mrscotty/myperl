#!/bin/bash

echo "INFO: HOME=$HOME"
echo "INFO: pwd"
pwd
echo "INFO: ls -latr"
ls -latr

make debian

echo "INFO: find / -name \*.deb"
find / -name \*.deb
