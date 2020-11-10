#!/usr/bin/env bash

rm -rf *.txt.selected
declare -a CNS=()

IFS=, read -r -a VALUES < genenames.txt
for key in "${VALUES[@]}"; do
    if [[ $key == *"_CN"* ]]; then
	cn_removed=$(echo $key | cut -d"_" -f 1)
        CNS+=("$cn_removed")
    fi
done

echo ${#CNS[@]}

select_cns() {
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
    {
        if ($1 in cnskeys) {
	    print $0;
        }
    }' $1 > $1.selected
}

for fname in $(ls *CNs.txt | xargs); do
    select_cns $fname
done
