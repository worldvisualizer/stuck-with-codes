#!/usr/bin/env bash

function check_installed() {
  if ! command -v $1 &> /dev/null; then
    echo "$1 not installed, script exiting"
    exit 1
  fi
}

check_installed brew
brew install fish

echo "chsh -s /usr/local/bin/fish" >> ~/.bashrc
source ~/.bashrc
