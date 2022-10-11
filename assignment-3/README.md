Assignment #3

This might be a bit scuffed. I'm not the best at coding plus I 
unavailable to attend this class but here it my attempt at the
assignment.





In the "etc" bin there is a bunch of .ma files. 
The "catfinder9000.aliases" file is supposed to look through all
of the .ma files and print all of the files containing "maine coon."
Not sure if I did this one quiet right.

In the "bin" folder is a script called "directory_maker.sh" that make 
a folder diectory. 
This script works but I can't seem to call on it despite following the
intruction and attempts at trouble shooting it.


In the "python" folder is a python script that makes an empty group in
maya named "empty_group".
This one works perfectly as far as I can tell. Just load it up with Maya's
script editor and execute it.





Below is my bash command for Part01 and Part02 of the assignment incase
you can't open the .aliases and .sh file.

Part01:
$ alias asset='echo | ls | grep "maine coon" | tr "." " "' > catfinder9000.aliases

Part02:
$export asset=project | mkdir -p "assets/$asset/maya/scenes" > directory_maker.sh



