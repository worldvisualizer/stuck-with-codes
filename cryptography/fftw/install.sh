#!/bin/bash

# download fftw 3.3.10
wget https://www.fftw.org/fftw-3.3.10.tar.gz
tar zvxf fftw-3.3.10.tar.gz

# install
pushd .
cd fftw-3.3.10
./configure
make -j
sudo make install

# remove unnecessary codes
popd
rm -rf fftw-3.3.10*
