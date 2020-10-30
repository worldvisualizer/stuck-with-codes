#!/bin/awk -f
BEGIN {
    # setting built-in variables as well as user-defined ones
    FS=":"; # input field separator
    OFS=":"; # output field separator
    lines=0;
    total=0;
}
{
    if ( $0 ~ /:/ ) {
	if (NR > 100) { # NR: current line number
	    print NR, $0; 
	}
        FS=":";
	$0=$0 # reevaluating fields
    } else {
        FS=" ";
	$0=$0
    }

    lines++;
    total+=$1;
    print $3
}
END {
    print lines " lines read";
    print total;
    if (lines > 0) {
        print "average is: ", total/lines;
    }
}
