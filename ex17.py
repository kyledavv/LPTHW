#imports argv function
from sys import argv
from os.path import exists
#imports exist function, returns true if does exist
script, from_file, to_file = argv
#prints Copying from 1st argument to 2nd argument
print(f"Copying from {from_file} to {to_file}")

# could do on one line
#opens from_file and makes it in_file
in_file = open(from_file)
indata = in_file.read()
#reads in_file and makes it indata
print(f"The input file is {len(indata)} bytes long")
#prints length of indata
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
#line 16 runs exist command to see if to_file exists. comes  back true.
#line 17 prints hit Return to continue, or ctrl c to abort.
#line 18 gives user input command to hit return or ctrl c
out_file = open(to_file, 'w')
out_file.write(indata)
#opens to_file to write, makes it out_file
#out_file writes indata
print("Arlight, all done.")
#prints alright, all done
out_file.close()
in_file.close()
#closed out_file
#closes in_file
