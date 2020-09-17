#!/usr/bin/env bash

VER=1.5.1

# problem with 1.0.5, notarization by apple required for OSX catalina
# https://github.com/JuliaLang/julia/issues/33331
curl https://julialang-s3.julialang.org/bin/mac/x64/1.5/julia-$VER-mac64.dmg -o julia-$VER-mac64.dmg
ln -s /Applications/Julia-1.5.app/Contents/Resources/julia/bin/julia /usr/local/bin/julia
