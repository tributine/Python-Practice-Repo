# Grid example character picture grid pp 103

grid = [['.','.','.'],
		['x','.','x'],
		['.','.','.'],
		['.','.','.'],
		['.','.','.']]

# we want gridup to look like:
# .x.
# .x.
# .x.

for i in grid:
	print(i)



for i in range(len(grid[0])):  # for the current number of elements in the list
	for k in range(len(grid)):	# print off each column as a row
		print(grid[k][i], end='')
	print('')

print(len(grid[0]))  # number of elements in the first list
print(len(grid))	 # number of  lists within the list of lists
