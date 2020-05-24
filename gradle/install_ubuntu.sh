#!/usr/bin/env bash

# check java version, should be 1.8.0 or higher
java -version
sdk install gradle 6.4.1 # version 6.4.1 is stable

# manual installation in comments
# wget https://gradle.org/next-steps/?version=6.4.1&format=all
# $ mkdir /opt/gradle
# $ unzip -d /opt/gradle gradle-6.4.1-bin.zip
# $ ls /opt/gradle/gradle-6.4.1
# $ export PATH=$PATH:/opt/gradle/gradle-6.4.1/bin

gradle -v