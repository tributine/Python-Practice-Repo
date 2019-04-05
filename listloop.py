tableData = [['applesaaaaaa', 'oranges', 'cherries', 'bananaaaa'],
            ['alice','Bob', 'Carol', 'David'],
            ['dogs','cats', 'moose', 'goose']]


colWidths = [0] * len(tableData)

for y in range(len(tableData)):
    for x in tableData[y]:
        print(len(x))
        print(colWidths[y])
        if colWidths[y] < len(x):
            colWidths[y] = len(x)


# Prints out the list of lists and right justify's it to the correct width
for a in range(len(tableData[0])):
    for b in range(len(tableData)):
        print(tableData[b][a].rjust(colWidths[b]), end=' ')
    print()
#
#colWidths = [0] * len(tableData)
#print(colWidths[0])
#print(colWidths[1])
#print(colWidths[2])
#print(tableData[0])
#print(len(tableData[0]))
#print(len(tableData))
