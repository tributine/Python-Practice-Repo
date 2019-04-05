# Name: Cw
# Project: Takes a string and flips it in reverse

text = input('What would you like to reverse: ') # This is the string to be reversed taken from clipboard
type(text)
textrev = '' # Reverse string variable

# Let's reverse THIS

# Create a decrementing for loop that starts from the full length - 1
for i in range((int(len(text) - 1) ),-1 ,-1): # Iterate in reverse through string
    textrev += text[i] # Text2 = previous character + new character

print(textrev) # Copy the reversed string into the clipboard
