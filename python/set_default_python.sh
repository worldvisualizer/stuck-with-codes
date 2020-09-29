#!/usr/bin/env bash

# changes python from default python (2.7.15) to python3.6, in this example
# applies for ubuntu.

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
# update-alternatives: using /usr/bin/python3.6 to provide /usr/bin/python (python) in auto mode
sudo update-alternatives --config python
# There is only one alternative in link group python (providing /usr/bin/python): /usr/bin/python3.6
# Nothing to configure.
sudo update-alternatives --config python3
# update-alternatives: error: no alternatives for python3
python --version
# Python 3.6.9
