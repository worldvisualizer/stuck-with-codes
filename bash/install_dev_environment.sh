#!/usr/bin/env bash

function check_installed() {
  if ! command -v $1 &> /dev/null; then
    echo "$1 not installed, script exiting"
    exit 1
  fi
}

check_installed brew
brew install coreutils
echo 'export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"' >> ~/.bashrc
echo 'export MANPATH="/usr/local/opt/coreutils/libexec/gnuman:$MANPATH"' >> ~/.bashrc
echo 'alias ls="ls --color"' >> ~/.bashrc
echo 'alias l="ls -lah"' >> ~/.bashrc
source ~/.bashrc
