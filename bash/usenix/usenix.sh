#!/usr/bin/env bash

# lots of these are linux specific - going with ubuntu

# The System
id # know yourself
w # who's logged in
lsblk # block storage devices
lscpu # cpu info
lstopo # hardware topology
free # free and used memory
lsb_release -a # distribution info

# The Process
ps aux
top
htop
atop
nice -n 19 tar cvzf archive.tgz large_dir
kill -9 1000000 # nonexistent stuff

# The Help
man nano
wget --help 
info curl
ls /usr/share/doc

# Working with Files
cat states.txt # short files
less /etc/ntp.conf
tail -f filename # watch file growing live
strings filename # print printable strings of file
od filename # print in octal format
cmp filename1 filename2 # compare byte by byte
comm filename1 filename2 # compare sorted files line by line
diff filename1 filename2

# The Internet
curl -O http://www.gutenberg.org/files/4300/4300-0.txt
curl ifconfig.me # quickly find my ip

wget http://www.gutenberg.org

lynx text.npr.org