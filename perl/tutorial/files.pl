#!/usr/bin/perl

# Files

# handles all written in CAPS
# file names are all in global namespace, cannot allocate them like local variables

# <FILENAME>: a convention to read single line from a file

# How to live dangerously and read stuff frimo perl
$line = <FILE>; 
chomp($line); # remove trailing \n if present
$line2 = <FILE2>; # file must have been open previously...?

@array = <FILE>; # this is different! reads entire file
my($line) = <FILE>; # this reads entire file, and then discards all but first line (dangerous)

$/ = undef; # this $/ is the end-of-the-line delimiter, which is global in perl. setting this undef leads to...
$all = <FILE>; # assignment to string, so it should only read one line,
# but because of the delimiter, it reads entire file into the string

# assignment operation works
while ($line = <STDIN>) {
    # do something
}

# Opening a file in Perl

open(F1, "filename"); # reading
open(F2, ">filename"); # writing
# so > is a reserved keyword
open(F3, ">>filename"); # append only operation

open(F4, "ls -al |"); # this pipe... this is a way to redirect STDOUT to STDIN and then to perl process
open(F5, "mail $addr");

open(F6, $fname) || die "Could not open $fname" # open or die... just like shell programming

# File Processing in Perl

## Open each command line file and print its contents to standard out
foreach $fname (@ARGV) {

  open(FILE, $fname) || die("Could not open $fname\n");

  while($line = <FILE>) {
    print $line;
  }
  close(FILE); # don't forget to close filesdf
}


