#!/usr/bin/perl -v

# Regex Matching with Perl, let's learn PGRE

($string -= /pattern/); # this gets the pattern worked out?
# true if pattern is found: what is that boolean?

"""
a, X, 9 -- ordinary characters just match that character exactly
. (a period) -- matches any single character except "\n"
\w -- (lowercase w) matches a "word" character: a letter or digit [a-zA-Z0-9]
\W -- (uppercase W) any non word character
\s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]
\S -- (uppercase S) any non whitespace character
\t, \n, \r  -- tab, newline, return
\d -- decimal digit [0-9]
\   -- inhibit the "specialness" of a character. 
"""
# So, for example, use \. to match a period or \\ to match a slash.
# If you are unsure if a character has special meaning, such as '@', 
# you can always put a slash in front of it \@ to make sure it is treated just as a character.

"""
#### Search for the pattern 'iiig' in the string 'piiig'
"piiig" =~ m/iiig/ ==> TRUE

#### The pattern may be anywhere inside the string
"piiig" =~ m/iii/ ==> TRUE

#### All of the pattern must match
"piiig" =~ m/iiii/ ==> FALSE

#### . = any char but \n
"piiig" =~ m/...ig/ ==> TRUE

"piiig" =~ m/p.i../ ==> TRUE

#### The last . in the pattern is not matched
"piiig" =~ m/p.i.../ ==> FALSE

#### \d = digit [0-9]
"p123g" =~ m/p\d\d\dg/ ==> TRUE

"p123g" =~ m/p\d\d\d\d/ ==> FALSE

#### \w = letter or digit
"p123g" =~ m/\w\w\w\w\w/ ==> TRUE

#### i+ = one or more i's
"piiig" =~ m/pi+g/ ==> TRUE

#### matches iii
"piiig" =~ m/i+/ ==> TRUE

"piiig" =~ m/p+i+g+/ ==> TRUE

"piiig" =~ m/p+g+/ ==> FALSE

#### i* = zero or more i's
"piiig" =~ m/pi*g/ ==> TRUE

"piiig" =~ m/p*i*g*/ ==> TRUE

#### X* can match zero X's
"piiig" =~ m/pi*X*g/ ==> TRUE

#### ^ = start, $ = end
"piiig" =~ m/^pi+g$/ ==> TRUE

#### i is not at the start
"piiig" =~ m/^i+g$/ ==> FALSE

#### i is not at the end
"piiig" =~ m/^pi+$/ ==> FALSE

"piiig" =~ m/^p.+g$/ ==> TRUE

"piiig" =~ m/^p.+$/ ==> TRUE

"piiig" =~ m/^.+$/ ==> TRUE

#### g is not at the start
"piiig" =~ m/^g.+$/ ==> FALSE

#### Needs at least one char after the g
"piiig" =~ m/g.+/ ==> FALSE

#### Needs at least zero chars after the g
"piiig" =~ m/g.*/ ==> TRUE

#### | = left or right expression
"cat" =~ m/^(cat|hat)$/ ==> TRUE

"hat" =~ m/^(cat|hat)$/ ==> TRUE

"cathatcatcat" =~ m/^(cat|hat)+$/ ==> TRUE

"cathatcatcat" =~ m/^(c|a|t|h)+$/ ==> TRUE

"cathatcatcat" =~ m/^(c|a|t)+$/ ==> FALSE

#### Matches and stops at first 'cat'; does not get to 'catcat' on the right
"cathatcatcat" =~ m/(c|a|t)+/ ==> TRUE

#### ? = optional
"12121x2121x2" =~ m/^(1x?2)+$/ ==> TRUE

"aaaxbbbabaxbb" =~ m/^(a+x?b+)+$/ ==> TRUE

"aaaxxbbb" =~ m/^(a+x?b+)+$/ ==> FALSE

#### Three words separated by spaces
"Easy      does it" =~ m/^\w+\s+\w+\s+\w+$/ ==> TRUE

#### Just matches "gates@microsoft" -- \w does not match the "."
"bill.gates@microsoft.com" =~ m/\w+@\w+/ ==> TRUE

#### Add the .'s to get the whole thing
"bill.gates@microsoft.com" =~ m/^(\w|\.)+@(\w|\.)+$/ ==> TRUE

#### words separated by commas and possibly spaces
"Klaatu,   barada,nikto" =~ m/^\w+(,\s*\w+)*$/ ==> TRUE

"""

# In Regex, we need several things: 1) matching groups, 2) substitution, 3) ? trick

# Matching
$str = 'blah blah nick@cs.stanford.edu, blah blah balh billg@microsoft.com blah blah';

while ($str =~ /(([\w._-]+)\@([\w._-]+))/) { ## look for an email addr
  print "user:$2 host:$3  all:$1\n";         ## parts of the addr
  $str = $';       ## set the str to be the "rest" of the string
}

# output:
# user:nick host:cs.stanford.edu  all:nick@cs.stanford.edu
# user:billg host:microsoft.com  all:billg@microsoft.com

# Substitution

$x = "This dress exacerbates the genetic betrayal that is my Legacy.\n";
$x =~ s/(r|l)(\w)/w$2/ig;    ## r or l followed by a word char
# The replacement pattern can use $1, $2 to refer to parts of the matched string. 
# The "g" modifier after the last / means do the replacement repeatedly in the target string. 
# The modifier "i" means the match should not be case sensitive.

## Change "r" and "l" followed by a word char to "w" followed
## by the same word char (this means just changing the phonetics effect)
## $x is now "This dwess exacewbates the genetic betwayal that is my wegacy."

# ? Trick to come. Argh this is dense

