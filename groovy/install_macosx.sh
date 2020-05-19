#!/bin/bash

curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk version
sdk install groovy

# now you can run:
groovy --version

# helpful invocation could be:
# groovyConsole
