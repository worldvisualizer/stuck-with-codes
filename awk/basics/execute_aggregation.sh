#!/usr/bin/env bash

rm -rf *.txt.selected*
declare -a VARS=()

IFS=, read -r -a VALUES < genenames.txt
for key in "${VALUES[@]}"; do
    if [[ $key == *"_CN"* ]]; then
        continue
    else
        VARS+=("$key")
    fi
done

echo ${#VARS[@]}

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
	if ($3 == "Y") {
	    print $0;
        }
    }' $1 >> $1.selected
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
        }
        if ($1 != prevcaseid) {
            prevcaseid = $1;
            casecount++;
        }
	if ($3 == "Y") {
	    y_chrs[casecount] = 1;
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
	    # add intercept portion
            str = str" "1;
            # add y_chr portion
	    y_val = 0;
	    if (y_chrs[j] == "1") {
		y_val = 1;
	    }
            str = str" "y_val;

            print str;
        }
    }' $1 > $1.aggregate
}

for fname in $(ls *variants.txt | xargs); do
    select_variants $fname
    aggregate_variants $fname.selected
done
