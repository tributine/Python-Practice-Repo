# 1. dict = {}
# 2. dict = {'foo': 42}
# 3. dictionary = assign keys to values, list = ordered series of values
# 4. Error as 'foo' does not exist in spam. There needs to be a default setup.
# 5. spam.keys() returns the keys in the dictionary 
# 6. spam.values() returns the values of the keys in the dictionary
# 7. use the setdefault command. "spam.setdefault('color', 'black')
# 8. import the prettyprint dictionary. pprint() 

# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items(): # k = 'rope etc.', v = int value of item
		#do this part
		print(k + ' ' + str(v))
		item_total = item_total + v
	#print(str(displayInventory(stuff)))
	print("Total number of items: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
	# code goes here
	# convert 'addedItems' to a list
	for loot in addedItems:
		inventory.setdefault(loot, 0)
		inventory[loot] += 1
	return(inventory)




inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coisn', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

#addedItems takes dragonLoot list of strings and converts it to dictionary, dictionarys are then added together
