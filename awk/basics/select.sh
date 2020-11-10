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
        # if ($2 in varskeys) {
        #     print $0;
        # }
	if ($3 == "Y") {
	    print $0;
        }
    }' $1
}

for fname in $(ls *variants.txt | xargs); do
    select_variants $fname
done
