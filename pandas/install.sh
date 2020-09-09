#!/usr/bin/env bash

ENV=pandas-env
if [ -d $ENV ]; then
    source $ENV/bin/activate
    python3 -m pip install -r requirements.txt
else
    python3 -m venv $ENV
fi

