#!/usr/bin/env bash

awk '
BEGIN {
    keys["ad"] = "aaa";
    keys["ae"] = "bbb";
    dumpvar = "DUMP";
}
{
    if ($1 in keys) {
	print "gotcha bitch";
	dumps[dumpvar","$1] = 1;
	print keys[$1];
    } else {
        print "what?!";
    }
    codaline[NR] = $1;
}
END {
    for (i = 1; i <= NR; i++) {
        print codaline[i];
    }
    print dumps["DUMP,ad"];
}
' inputfile
