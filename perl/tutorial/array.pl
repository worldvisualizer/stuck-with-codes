#!/usr/bin/perl

# Arrays -- @

# array constants: ()
# perl arrays can grow and shrink but still called arrays. 
# assignment operator = works: independent deepcopy made.
# 1-deep mentality: no array inside an array

@array = (1,2, 'hello');
@empty = ();

$x = 1;
$y = 2;
@nums = ($x + $y, $x - $y);

# @nums is now (3, -1)

@array = (1, 2, "hello", "there");
$array[0] = $array[0] + $array[1];    ## $array[0] is now 3
# note that the array elements are referred to as scalar.

$array[0] # front of the array
$array[$len - 1] # end of the array.

@array = (1, 2, "hello", "there");
$sum = $array[0] + $array[27];
## $sum is now 1, since $array[27] returned undef
$array[99] = "the end";
 ## array grows to be size 100

# When used in a scalar context, an array evaluates to its length
# The "scalar" operator will force the evaluation of something
# in a scalar context, so you can use scalar()
# to get the length of an array.
# As an alternative to using scalar, the expression $#array
# is the index of the last element of the array which is
# always one less than the length.

@array = (1, 2, "hello", "there");
$len = @array;                ## $len is now 4 (the length of @array)

$len = scalar(@array)         ## same as above, since $len represented a scalar
                              ## context anyway, but this is more explicit

@letters = ("a", "b", "c");
$i = $#letters;               ## $i is now 2

# (sort @a): gives a copy of a sorted @a.
(sort @array)                       
## sort alphabetically, with uppercase first
(sort {$a <=> $b} @array)            
## sort numerically
(sort {$b cmp $a} @array)            
## sort reverse alphabetically
(sort {lc($a) cmp lc($b)} @array)    
## sort alphabetically, ignoring case (somewhat inefficient)

($x, $y, $z) = (1, 2, "hello", 4);
## assigns $x=1, $y=2, $z="hello", and the 4 is discarded
# This type of assignment only works with scalars.
# If one of the values is an array,
# the wrong thing happens (see "flattening" below).

$elem = shift(@array) # remove at the first index
unshift(@array, $elem) # insert at the first index, returns length of the array
$elem2 = pop(@array)
push(@array, $elem) # push at the end, returns length of the array
splice(@array, $index, $length, @array2)

