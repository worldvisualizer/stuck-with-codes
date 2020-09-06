#!/usr/bin/env bash

VERSION=$1
if [ -z "$var" ]; then
    echo "you need to set the version of the Golang. Recommended: 1.15"
fi

EXEC=go$VERSION.linux-amd64.tar.gz

wget https://dl.google.com/go/$EXEC
sha256sum $EXEC

read -p "Checksum matches? Type 'yes' to continue installation" matched

if [ "$matched" = "yes" ]; then
    sudo tar -C /usr/local -xzf $EXEC
    echo 'PATH=$PATH:/usr/local/go/bin' >> /etc/profile
    source /etc/profile
fi

go version
  
