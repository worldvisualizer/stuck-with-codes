#!/usr/bin/env bash

curl https://julialang-s3.julialang.org/bin/mac/x64/1.0/julia-1.0.5-mac64.dmg -o julia-1.0.5-mac64.dmg 
ln -s /Applications/Julia-1.0.app/Contents/Resources/julia/bin/julia /usr/local/bin/julia
