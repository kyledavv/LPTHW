#Pig latin Translator in Python2.7

if len(word) > 0 and word.isalpha():
    str.lower(word)

else:
        print 'empty'

print new_word

#sets variable pyg
pyg = 'ay'
#gets user to input a word, called original
original = input('Enter a word:')
#need syntax. returns original word to lowercase, now called word
word = original.lower()
#singles out first letter in word, first letter called first
first = word[0]
#creates piglatin word with three variables
new_word = word[1:] + first + pyg
