#!/usr/bin/env bash

g++ -o tri triangle.cpp
./tri <<EOF
2
5
2 3 4 5 10
6
2 3 4 6 8 10
EOF

rm -rf tri
