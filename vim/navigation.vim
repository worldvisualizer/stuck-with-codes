vim <filename>   # Open <filename> in vim
:help <topic>    # Open up built-in help docs about <topic> if any exists
:q               # Quit vim
:w               # Save current file
:wq              # Save file and quit vim
ZZ               # Save file and quit vim
:q!              # Quit vim without saving file
                 # ! *forces* :q to execute, hence quiting vim without saving
ZQ               # Quit vim without saving file
:x               # Save file and quit vim, shorter version of :wq

u                # Undo
CTRL+R           # Redo

h                # Move left one character
j                # Move down one line
k                # Move up one line
l                # Move right one character

Ctrl+B           # Move back one full screen
Ctrl+F           # Move forward one full screen
Ctrl+D           # Move forward 1/2 a screen
Ctrl+U           # Move back 1/2 a screen 

# Moving within the line

0                # Move to beginning of line
$                # Move to end of line
^                # Move to first non-blank character in line

# Searching in the text

/word            # Highlights all occurrences of word after cursor
?word            # Highlights all occurrences of word before cursor
n                # Moves cursor to next occurrence of word after search
N                # Moves cursor to previous occerence of word

:%s/foo/bar/g    # Change 'foo' to 'bar' on every line in the file
:s/foo/bar/g     # Change 'foo' to 'bar' on the current line
:%s/\n/\r/g      # Replace new line characters with new line characters

# Jumping to characters

f<character>     # Jump forward and land on <character>
t<character>     # Jump forward and land right before <character>

# For example,
f<               # Jump forward and land on <
t<               # Jump forward and land right before <

# Moving by word

w                # Move forward by one word
b                # Move back by one word
e                # Move to end of current word

# Other characters for moving around

gg               # Go to the top of the file
G                # Go to the bottom of the file
:NUM             # Go to line number NUM (NUM is any number)
H                # Move to the top of the screen
M                # Move to the middle of the screen
L                # Move to the bottom of the screen
