#!/usr/bin/env bash

function copy_files() {
    local msg="$1"
    local msg2="$2"
    shift
    shift
    local arr=("$@")
    for i in "${arr[@]}"; do
        echo "$msg $msg2 $i"
    done
}

array=("joseph" "james" "brother")
copy_files "copying this: " "what are you looking at" "${array[@]}"
