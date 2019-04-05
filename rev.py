# Name: Climber
# Project: Takes a string and flips it in reverse
import pyperclip
text = pyperclip.paste() # This is the string to be reversed taken from clipboard
textrev = '' #T
# Let's reverse THIS

# Create a decrementing for loop that starts from the full length - 1
for i in range((int(len(text) - 1) ),-1 ,-1): # Iterate in reverse through string
    textrev += text[i] # Text2 = previous character + new character

pyperclip.copy(textrev) # Copy the reversed string into the clipboard



# Ex: i in range(25, -1, -1)
    # i would be 25 at first
    # print(text[0][25], end='')

# text is a list with a string. text[0] returns the string thus,
# text[0][i] returns the string character within the string in the list!
