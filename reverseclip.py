# Name: Climber
# Project: Takes a string and flips it in reverse
import pyperclip
text = [pyperclip.paste()] # This is the string to be reversed
text2 = ''
# Let's reverse THIS

# Create a decrementing for loop that starts from the full length - 1
for i in range((int(len(text[0]) - 1) ),-1 ,-1):
    #print(text[0][i], end='') # Iterate through the string character within the list
    text2 = str(text2) + text[0][i]


    #text[0] = text[0]
pyperclip.copy(text2)



# Ex: i in range(25, -1, -1)
    # i would be 25 at first
    # print(text[0][25], end='')

# text is a list with a string. text[0] returns the string thus,
# text[0][i] returns the string character within the string in the list!
