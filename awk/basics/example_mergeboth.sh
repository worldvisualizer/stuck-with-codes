#!/usr/bin/env bash

merge_both() {
    awk -v AV="$(printf '%s\1' "${CNS[@]}")" '
    BEGIN {
        na = split(AV, cnsvalues, "\\1");
        delete cnsvalues[na];
        for (i in cnsvalues) {
            cnskeys[cnsvalues[i]] = i;
        }
        FS=" ";
        OFS=" ";
    }
    NR > 1 {
        print $0
    }' $1 $2
}

merge_both inputfile inputfile2 
