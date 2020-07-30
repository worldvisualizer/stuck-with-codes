#!/usr/bin/env bash

function check_installed() {
  if ! command -v $1 &> /dev/null; then
    echo "$1 not installed, script exiting"
    exit 1
  fi
}

check_installed brew

# install nvm for stable nodejs release
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
source ~/.bashrc
nvm install v12.18.2
nvm use v12.18.2
node --version

# upgrade npm and install npx
npm install -g npm@latest
npm install -g npx 

