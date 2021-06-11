#!/usr/bin/env bash

g++ -o incr_substr increasing_substring.cpp

./incr_substr <<EOF
2
4
ABBC
6
ABACDA
EOF

