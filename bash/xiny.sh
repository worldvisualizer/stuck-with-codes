#!/usr/bin/env bash

# https://unix.stackexchange.com/questions/29608/why-is-it-better-to-use-usr-bin-env-name-instead-of-path-to-name-as-my
# interesting...

echo 'First line'; echo 'Second line, echo again'

# 1. variable declaration and assignment
variable='some string'
# whitespace is important

# using the variable
echo $variable # some string
echo "$variable" # some string
echo '$variable' # 'variable'

# 2. Parameter Expansion
echo ${variable}
# it gets a value from the variable and expands it
# during the expansion time the value or parameter can be modified

# 3. string manipulation scheme, as well as variable
echo ${variable/some/A} # substitution syntax 
length=7
echo ${#variable} # string length. special
echo ${variable:0:length}
echo ${variable:-5}
echo ${foo:-"Default value"}

# 4. array
array0=(one two three four five six)
echo $array0 # => one. this is like a pointer concept
echo ${array0[0]} # first element
echo ${array0[@]} # entire array elements
echo ${#array0[@]} # number of elements
echo ${#array0[2]} # number of characters in third element(!)
echo ${array0[@]:3:2} # print 2 elements from 4th element
for i in "${array[@]}"; do
    echo "$i"
done

# 5. Brace Expansion
# used to generate arbitrary strings
echo {1..10}
echo {a..z}

# 6. Built-in Variables
echo "last programs return value: $?"
echo "Script PID: $$"
echo "Number of arguments passed to script: $#"
echo "All arguments passed to script: $@"
echo "Script's arguments separated to vars: $1 $2 ..."
# execution and output interpolation
echo "I am in $(pwd)"
# interpolates variable, but this is preset before the script
echo "I am in $PWD"

echo "What's your name?"
read name # don't need to declare a new variable
echo Hello $name

# 7. Control Structure
if [ $name != $USER ]; then
    echo "oops username does not match"
else
    echo "user verified"
fi

# if name is empty... this happens:
# if [ != $USER ]
# which is invalid syntax
# so the "safe" way to use potentially empty variables in bash is:
if [ "$Name" != $USER ]; then
    echo "interpolation"
fi
# which, when $Name is empty, is seen by bash as:
if [ "" != $USER ]; then
    echo "this is always printed"
fi

echo "always executed" || echo "only executed if first command fails"
echo "always executed" && echo "only executed if first command does not fail"

# using && and || with if requires multiple pairs of square:
if [ "$name" == "seung-woo" ] && [ "$age" -eq 31 ]; then
    echo "user verified with age $age"
fi

# also a `=~` operator. tests string against a regex pattern:
email=seungwoo.jung89@gmail.com
if [[ "$email" =~ [a-z]+@[a-z]{2,}\.(com|net|org) ]]; then
    echo "valid email"
fi
# there are (( )) and [[ ]]
# (( )): shell arithmetic
# [[ ]]: return a status of 0 or 1 depending on the evaluation

# aliasing
alias ping='ping -c 5'
# escaping makes this name an executable command
\ping 127.0.0.1
alias -p  # print all aliases

# mathematical expressions: expressions follow context in bash
echo $(( 10 + 5 ))
# so this is possible
ten=10
five=5
echo $(( $ten + $five ))

touch file.txt
contents=$(cat file.txt)
# You can redirect command input and output
# (stdin, stdout, and stderr).
# Read from stdin until ^EOF$ and overwrite hello.py
# with the lines between "EOF"
# variables will be expanded if the first 
cat > hello.py << EOF
#!/usr/bin/env python
from __future__ import print_function
import sys
print("#stdout", file=sys.stdout)
print("#stderr", file=sys.stderr)
for line in sys.stdin:
    print(line, file=sys.stdout)
EOF

# Run the hello.py Python script with
# various stdin, stdout, and stderr redirections:

# pass input.in as input to the script
python hello.py < "input.in" 
# redirect output from the script to output.out
python hello.py > "output.out" 
# redirect error output to error.err
python hello.py 2> "error.err" 
# redirect output and errors 
python hello.py > "output-and-error.log" 2>&1
# redirect all output and errors to /dev/null
# /dev/null is a special file called the null device in unix
# immediately discards everything written and returns only EOF
# when read
python hello.py > /dev/null 2>&1
# output error will overwrite the file if it exists
# if want to append, then
python hello.py >> 'output.out' 2>> "error.log"

# example: overwrite output.out, append to error.err, count line
info bash "basic shell features" "redirections" > output.out 2>> error.err
wc -l output.out error.err

# Bash uses a `case` statement that works similarly to switch in Java and C++:
case "$Variable" in
    #List patterns for the conditions you want to meet
    0) echo "There is a zero.";;
    1) echo "There is a one.";;
    *) echo "It is not null.";;
esac # note that esac is used

for variable in {1..3}; do
    echo "$variable"
done # done. it's not fi.

for (( a=1; a <= 3; a++ )); do
    echo $a
done

# so this becomes filenames.
for variable in file1 file2; do
    cat $variable
done

for output in $(ls); do
    cat "$output"
done

while [ true ]; do
    echo "loop"
    break
done

function foo() {
    # function definitions
    return $1
}

# Call the function `foo` with two arguments, arg1 and arg2:
foo arg1 arg2
# => Arguments work just like script arguments: arg1 arg2
# => And: arg1 arg2...
# => This is a function
foo "My name is" $Name

