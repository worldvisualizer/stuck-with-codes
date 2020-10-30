#!/usr/bin/env bash

array=(GENE1 GENE2 GENE3 GENE4)

awk -v AV="$(printf '%s\1' "${array[@]}")" '
BEGIN {
    na = split(AV, array, "\\1")
    delete array[na]
    for (i = 1; i <= na-1; i++) {
        print "AV#", i, "=" array[i]
    }
}
{
    str=""
    for (i in array)
        str = str" "i" "$1
    print str
}' inputfile

