#!/usr/bin/env bash

FEATURESET=featureset

rm -rf $DATASET_PATH/*txt.selected*
rm -rf $FEATURESET

declare -a CNS=()
declare -a VARS=()
IFS=, read -r -a VALUES < ../genenames.txt
for key in "${VALUES[@]}"; do
    if [[ $key == *"_CN"* ]]; then
	continue
    else
        VARS+=("$key")
    fi
done


select_variants() {
    awk -v AV="$(printf '%s\1' "${VARS[@]}")" '
    BEGIN {
        na = split(AV, varsvalues, "\\1");
        delete varsvalues[na];
        for (i in varsvalues) {
            varskeys[varsvalues[i]] = i;
        }

        FS=" ";
        OFS=" ";
    }
    {
        if ($2 in varskeys) {
            print $0;
        }
    }' $1 > $1.selected
}

aggregate_variants() {
    awk -v AV="$(printf '%s\1' "${VARS[@]}")" '
    BEGIN {
        na = split(AV, varsvalues, "\\1");
        delete varsvalues[na];
        for (i in varsvalues) {
            varskeys[varsvalues[i]] = i;
        }

        casecount = 0;
        prevcaseid = "";
        FS=" ";
        OFS=" ";
    }
    {
        if ($2 in varskeys) {
            ind = varskeys[$2];
            indicator[$1","ind] = 1;
        } else {
            print $2 ": does not exist in varskeys"
        }
        if ($1 != prevcaseid) {
            prevcaseid = $1;
            casecount++;
        }
        casearray[casecount] = $1;
    }
    END {
        for (j = 1; j <= casecount; j++) {
            caseid = casearray[j];
            str = caseid;
            for (i in varsvalues) {
                val = 0;
                if (indicator[caseid","i] == 1) {
                    val = 1;
                }
                str = str" "val;
            }
            print str;
        }
    }' $1 > $1.aggregate
}

