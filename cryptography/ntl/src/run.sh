#!/usr/bin/bash

NAME=${1:-hello}
# -pthread option is to use the default multithreading enabled in NTL
# library option is ntl, gml, m
# -march=native option is to enhance performance for "specific" x86 architecture
# -lgf2x option is optional, if NTL was built with gf2x option.

# build with default arguments
g++ -g -O2 -std=c++11 -pthread -march=native $NAME.cpp -o exec -lntl -lgmp -lm

# run the executable
./exec
