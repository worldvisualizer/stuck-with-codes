#!/usr/bin/perl -w

# Syntax and Variables

# simple variables are called "scalar". if unassigned, "undef"
$x = 2; 
$greeting = "hello";

# undef is equivalent to 0 or "" when conditioned
if (!defined($binky)) {
  print "the variable 'binky' has not been given a value!\n";
}

# Strings

# "" string have \n, \x20 kind of capabilities compared to ''
$fname = "binky.txt";
$a = "Could not open the file $fname." # $fname evaluated
$b = 'Could not open the file $fname.' # nope.

## $a is now "Could not open the file binky.txt."
## $b is now "Could not open the file $fname."

# The characters '$' and '@' are used to trigger interpolation
# into strings, so those characters need to be escaped 
# with a backslash (\) 
# if you want them in a string. 
# For example: "nick\@stanford.edu found \$1".

# The dot operator (.) concatenates two strings.
# If Perl has a number or other type when it wants a string,
# it just silently converts the value to a string and continues.
# It works the other way too --
# a string such as "42" will evaluate to the integer 42
# in an integer context.
$num = 42;
$string = "The " . $num . " ultimate" . " answer";

## $string is now "The 42 ultimate answer"

# The operators eq (equal) and ne (not equal) compare two strings.
# Do not use == to compare strings; use == to compare numbers.

$string = "hello";
($string eq ("hell" . "o"))  ==> TRUE
($string eq "HELLO")  ==> FALSE

$num = 42;
($num-2 == 40)  ==> TRUE