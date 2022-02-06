#!/bin/bash

# download 11.5.1
wget https://libntl.org/ntl-11.5.1.tar.gz
tar xvzf ntl-11.5.1.tar.gz

pushd .
# set up and install NTL
# TODO: if additional args needed, put it here
cd ntl-11.5.1/src
./configure
make -j
make check
sudo make install

popd

# remove unnecessary sources
rm -rf ntl-11.5.1.tar.gz ntl-11.5.1
