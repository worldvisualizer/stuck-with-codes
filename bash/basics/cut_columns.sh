#!/usr/bin/env bash

# cut -f 1-10 -d "<CTR>v <TAB>" filtered_mock.csv
cut -d$',' -f 1-10 filtered_mock.csv
