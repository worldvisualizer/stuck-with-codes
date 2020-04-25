#!/usr/bin/perl

# Subroutines

# subroutines don't have to be defined before they are used
$x = Three();
exit(0);

sub Three {
	return (1 + 2); 
}

# in perl 5, 'my' construct allows local variables
my $a;
my $b = "hello";
my @array = (1,2,3);
my ($x, $y);
my ($a, $b) = (1, "hello"); # declare and assign multiple

sub Three {
	my ($x, $y);
	$x = 1;
	$y = 2;
	return ($x + $y);
}

sub Three2 {
	my ($x, $y) = (1,2);
	return ($x + $y);
}

# subroutines do not have named parameters...!
# so @_ (an array) is used to pass the parameters down
sub Sum1 {
	my ($x, $y) = @_;
	return ($x + $y);
}

# you can also pull out the values directly
sub Sum2 {
	return ($_[0] + $_[1]);
}

sub Sum3 {
	my ($sum, $elem);
	$sum = 0;
	foreach $elem (@_) { # foreach definition
		$sum += $elem;
	}
	return ($sum);
}

# just a variant of Sum3, defined...!?
sub Sum4 {
	my ($sum, $elem);
	$sum = 0;
	while (defined($elem = shift(@_))) {
		$sum += $elem;
	}
	return ($sum);
}

# File Handle Arguments

# file handles are all in a global namespace,
# so you cannot allocate them locally, but you can pass them
# to subroutines with file handlename as a string.

open(FILE, ">file.txt"); # so a file handle FILE is declared globally
SayHello("FILE"); # and it's passed in as a filename
close(FILE);

sub SayHello {
	my ($filehandle) = @_;
	print $filehandle "I am a little teapot"; # prints to the file
}

# Return multiple values to the caller

sub DoSomething {
	return (-13, "Darn!"); # return an array len 2
}

my ($num, $string) = DoSomething(); # a call
if ($num < 0) {
	print "Gasp\n"; 
}

# Flattened Arguments

Sum3(1,2, (3,4)); # argument array is automatically Flattened
# this property can hurt you
my (@nums, $three) = ((1,2),3);
# this leads to @nums = (1,2,3);, $three = undef;
# so always beware!
# workaround: storing references to arrays in other arrays

# Global variables and 'use strict';

use strict 'vars'; # enforce local/global var declarations
use strict; # additional style checks

# with strict vars, variables inside functions must be my().

## With strict vars...

## 1. Undeclared global vars must begin with "::" at all times
$::global = 13;

## 2. Or a global may be declared with a my(), in which case
## the :: is not necessary
my $global2 = 42;

sub foo {
  my $sum;
  $sum = $::global + $global2;
  ## $sum and $global2 work without extra syntax
  return($sum);
}

