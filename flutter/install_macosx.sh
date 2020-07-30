#!/usr/bin/env bash

INSTALLPATH=/usr/local/bin
cd $INSTALLPATH
unzip ~/Downloads/flutter_macos_1.17.5-stable.zip
BASHRCPATH="PATH=$PATH:$INSTALLPATH/flutter/bin"
echo $BASHRCPATH >> $HOME/.bashrc
source $HOME/.bashrc
flutter doctor
