# table printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['alice']]
print(len(tableData))

def printTable(table):
    flat_list = []
    for sublist in table:
        for item in sublist:
            flat_list.append(item)
    #flat_list = flat_list.split('\n')
    for i in range((len(flat_list))):
        flat_list[i] = '\n' + flat_list[i]
    flat_list = ''.join(flat_list)
    print(flat_list)

printTable(tableData)
