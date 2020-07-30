#!/usr/bin/env bash

RUBY_VERSION=${1:-"2.7.0"}

# install and download softwares
brew install gpg
sudo gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | sudo bash -s stable
sudo usermod -a -G rvm `whoami`

# figuring out if sudo is configured with secure_path
if sudo grep -q secure_path /etc/sudoers; then sudo sh -c "echo export rvmsudo_secure_path=1 >> /etc/profile.d/rvm_secure_path.sh" && echo Environment variable installed; fi

# check rvm version
rvm -v

# install ruby version you want
rvm install ruby-$RUBY_VERSION
rvm --default use ruby-$RUBY_VERSION

# install bundler
gem install bundler --no-rdoc --no-ri

