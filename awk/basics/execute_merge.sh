#!/usr/bin/env bash

rm -rf featureset

merge_both() {
    awk '
    BEGIN {
        FS=" ";
        OFS=" ";
    }
    NR > 1 {
        # loading in variants
        if ($1 in casekeys) {
            # loading in variants
	    sofar = casekeys[$1];
	    for (i = 2; i <= NF; i++) {
	        sofar = sofar " " $i;
	    }
            casekeys[$1] = sofar;
            
	} else {
	    # loading in CNs
	    sofar = $2;
	    for (i = 3; i <= NF; i++) {
		sofar = sofar " " $i;
	    }
            casekeys[$1] = sofar;
        }
    }
    END {
	for (caseid in casekeys) {
            print caseid " " casekeys[caseid];
        }
    }' $1 $2 >> featureset
}

merge_both Bladder_challenge_CNs.txt.selected.transpose Bladder_challenge_variants.txt.selected.aggregate
