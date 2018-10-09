#Pig Translator in Python3.6

#set up input command to see which word to translate
original = input("Enter a word ->")

word = original.lower()

pyg = 'ay'

first = word[0]

pyg_word = word[1:] + first + pyg

if len(word) > 0 and word.isalpha():
    print('Word')

else:
    print ("empty")

print (pyg_word)
