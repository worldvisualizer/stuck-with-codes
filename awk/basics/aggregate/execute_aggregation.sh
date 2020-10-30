#!/usr/bin/env bash


declare -a VARS=()

aggregate_variants() {
    awk '
    BEGIN {
        FS=" "
	OFS=" "
    }
    { 
        for (i=1; i<=NF; i++)  {
	    if (VARS
            a[NR,i] = $i
        }
    }
    NF>p { p = NF }
    END {    
        for(j=1; j<=p; j++) {
            str=a[1,j]
            for(i=2; i<=NR; i++){
                str=str" "a[i,j];
            }
            print str
        }
    }' $1 >> $1.transpose
}

IFS=, read -r -a VALUES < genenames.txt
for key in "${VALUES[@]}"; do
    if [[ $key == *"_CN"* ]]; then
    	continue
    else
        VARS+=("$key")
    fi
done

echo ${#VARS[@]}
