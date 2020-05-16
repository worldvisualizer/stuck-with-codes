>                # Indent selection by one block
<                # Dedent selection by one block
:earlier 15m     # Reverts the document back to how it was 15 minutes ago
:later 15m       # Reverse above command
ddp              # Swap position of consecutive lines, dd then p
.                # Repeat previous action
:w !sudo tee %   # Save the current file as root
:set syntax=c    # Set syntax highlighting to 'c'
:sort            # Sort all lines
:sort!           # Sort all lines in reverse
:sort u          # Sort all lines and remove duplicates
~                # Toggle letter case of selected text
u                # Selected text to lower case
U                # Selected text to upper case

# Fold text
zf               # Create fold from selected text
zo               # Open current fold
zc               # Close current fold
zR               # Open all folds
zM               # Close all folds
