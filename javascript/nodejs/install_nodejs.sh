#!/usr/bin/env bash

# install nvm for stable nodejs release
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | sh
source ~/.bashrc
nvm install v12.18.2
nvm use v12.18.2
node --version

# upgrade npm and install npx
npm install -g npm@latest

# npx is already installed in nodejs 12.18
# npm install -g npx 

