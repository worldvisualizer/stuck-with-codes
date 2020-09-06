#!/usr/bin/env bash

brew update && brew install golang

echo 'export GOPATH=$HOME/go
export GOROOT="$(brew --prefix golang)/libexec"
export PATH="$PATH:${GOPATH}/bin:${GOROOT}/bin"' >> /etc/profile
source /etc/profile
