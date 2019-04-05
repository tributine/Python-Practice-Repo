grid = [['.', '.', '.', '.', 'x'],
		['.', '.', '.', 'x', '.'],
		['.', '.', 'x', '.', '.']]


for j in range(len(grid)):
	for k in range(len(grid[0])):
		print(grid[j][k], end='')
	print('')