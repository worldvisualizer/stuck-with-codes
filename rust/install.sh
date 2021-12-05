#!/usr/bin/env bash

# recommended installation
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

source $HOME/cargo/.env
rustc --version # Rust compiler
rustup show # Rust's toolchain manager
cargo --version # Rust's package manager
