formatter = "{} {} {} {}"
#sets the formatter string
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
#prints 1,2,3,4 and one, two, three, four on the next line
print(formatter.format(True, False, False, True))
#prints True, False, False, True
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
)) #puts everything in one line, regardless of putting in on a different line
