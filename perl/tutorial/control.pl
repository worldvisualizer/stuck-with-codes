#!/usr/bin/perl

# If/While Syntax

# it kind of looks like C's control syntax.
# there's no boolean type!!!
# the empty string, the empty array,
# the number 0 and undef all evaluate to false,
# and everything else is true.

if (expr) {         ## basic if -- ( ) and { } required
  stmt;
  stmt;
}
if (expr) {         ## if + elsif + else
  stmt;
  stmt;
}
elsif (expr) {      ## note the strange spelling of "elsif"
  stmt;
  stmt;
}
else {
  stmt;
  stmt;
}

unless (expr) {     ## if variant which negates the boolean test
  stmt;
  stmt;
}

# modifier structure possible after single statement
$x = 3 if $x > 3;  ## equivalent to: if ($x > 3) { $x = 3; }
$x = 3 unless $x <= 3;

# Loops 

while (expr) {
 stmt;
 stmt;
}

for (init_expr; test_expr; increment_expr) {
 stmt;
 stmt;
}

## typical for loop to count 0..99
for ($i=0; $i<100; $i++) {
 stmt;
 stmt;
}

# foreach
foreach $var (@array) {
  stmt;    ## use $var in here
  stmt;
}
# iterating variable, such as $var,
# is actually a pointer to each element in the array,
# so assigning to $var will actually change the elements

