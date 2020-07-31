#!/usr/bin/env bash

# sets up flutter and set its path
INSTALLPATH=/usr/local/bin
cd $INSTALLPATH
unzip ~/Downloads/flutter_macos_1.17.5-stable.zip
BASHRCPATH="PATH=$PATH:$INSTALLPATH/flutter/bin"
echo $BASHRCPATH >> $HOME/.bashrc
source $HOME/.bashrc

# this assumes android studio is installed
flutter doctor --android-licenses

# configure xcode related stuff
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch
ruby -v
sudo gem install cocoapods

