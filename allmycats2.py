catNames = []  # Create a list called catnames
while True:    # Always loop until break occurs
	print('Enter the name of cat ' + str(len(catNames) + 1) + 
		' (or enter nothing to stop)')	
	name = input("What's your name? ")
	if name == '':
		break
	catNames = catNames + [name] # Add to cat list the input cat name
print('The cat names are')
for name in catNames:
	print(' ' + name)