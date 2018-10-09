import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.script()
    raw_bytes = next_lang.encode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

    langugages = open("languages.txt", encoding="utf-8")

    main(languages, encoding, error)

#LINE BREAK DOWN OF CODE
#Lines 1-2: usual command line argument handling
#Line 5: main meat of code with main function. will be called at the end of the script to get things going
#Line 6: Fuction to read one line from the langugages file it was given. readline to read the text files
#Line 8: lets you make decisions in your python code. can test the truth of a variable and run a piece of
    #code or not based on that truth. Testing whether line has something in it. Readline will return
    #empty string when it reaches the end of the file and if file simply tests for the empty string
#Line 9: Separate function to do the actual printing of this line. Simplifies code and makes it easier to
    #understand.
#Line 10: calling main inside of main. creatses a loop that will run until the if-statement returns false
#Line 13: start the definition of print_line function, does the actual encoding of each line from languages.txt file
#Line 14: simple stripping of the trailing \n on the line string
#Line 15: finally take the language i've received from the languages.txt file and encode it into the raw bytes.
    #DBES: Decode bytes, encode strings
    #next_lang variable is a string, so to get the raw bytes i must call .encode() on it to encode the strings.
    #i pass to encode() the encoding i want and how to handle errors
#Line 16: do the extra step of showing the inverse of line 15 by creating a cooked_string variable from raw_bytes.
#Line 18: simply prints them both out to show you what they look like
#Line 21: Im done defining functions, so now i want to open the languages.txt file
#Line 23: the end of the script simply runs the main function with all the correct parameters to get everything going
    #and kick start the loop. This then jumps up to first main function on line 5, then main is called again on line 10,
    #and the if line: is what stops the loop from going forever
