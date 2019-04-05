#! python3
# Name: Christopher wong
# filename: bulletPointAdder
# Description: Adds bulletpoints infront of each line of text

import pyperclip
text = pyperclip.paste() # text = whatever we have copied
# Todo: Separate lines and add stars.

pyperclip.copy(text)
# current clip looks like 'food\nshelter\neducation' etc all separated by \n
#separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in lines list
#text = '\n'.join(lines)
pyperclip.copy(text)
