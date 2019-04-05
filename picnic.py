allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, # Dictionary of dictionaries
			'Bob': {'ham sandwiches': 3, 'apples': 2},
			'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
	numBrought = 0
	for k, v in guests.items():	# string of guests name assigned to k, dictionary picnic items they are bringing is v
		numBrought = numBrought + v.get(item,0) # numBrought will iterate through each guest and add the corresponding item and quantity for that item
	return numBrought

print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(allGuests.get('Alice', 0).get('apples',0)) # first get for Alice dictionary, second get for apples dictionary
