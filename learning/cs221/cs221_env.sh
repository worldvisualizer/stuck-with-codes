#!/usr/bin/env bash

DIRECTORY=cs221-env

if [ ! -d "$DIRECTORY" ]; then
    python3 -m venv $DIRECTORY
    
fi
source $DIRECTORY/bin/activate
