#!/usr/bin/perl

# Hash Arrays -- %

# hash arrays are built-in key/value data structure
# if no such key in the array, value returned is undef
# keys are case sensitive

$dict{"bart"}  = "I didn't do it";
$dict{"homer"} = "D'Oh";
$dict{"lisa"}  = "";

## %dict now contains the key/value pairs
# (("bart" => "I didn't do it"), ("homer" => "D'oh"), ("lisa" => ""))

$string = $dict{"bart"};     ## Lookup the key "bart" to get
                             ## the value "I didn't do it"

$string = $dict{"marge"};    ## Returns undef -- there is no entry for "marge"

$dict{"homer"} = "Mmmm, scalars";    
## change the value for the key "homer" to "Mmmm, scalars"

@array = %dict;
## @array will look something like
##  ("homer", "D'oh", "lisa", "", "bart", "I didn't do it");
##
## (keys %dict) looks like ("homer", "lisa, "bart")
## or use (sort (keys %dict))

# another way of writing hash
%dict = (
  "bart" => "I didn't do it",
  "homer" => "D'Oh",
  "lisa" => "",
);

@ARGV # built in array, has command line arguments.
>> perl critic.pl -poetry poem.txt
# ("-poetry", "poem.txt")

