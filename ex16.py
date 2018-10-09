from sys import argv
#imports argv
script, filename = argv
#We're going to erase the filename typed in
#If not, hit ctrl c
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#if yes, hit return
input("?")
#shows ? for the input from user
print("Opening the file...")
target = open(filename, 'w')
#open the said filename
print("Truncating the file. Goodbye!")
target.truncate()
#deleting the file contents
print("Now I'm going to ask you for three lines.")
#ask for three lines. user inputs into the system with line 1,2,3 prompt
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
#prints "I'm going to write these to the file."
print("I'm going to write these to the file.")
#writes the inputs to the file
target.write()



#close the file
print("And finally, we close it.")
target.close()
