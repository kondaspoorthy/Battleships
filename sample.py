import battleship_tests as tet
EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4
def emptyGrid(row,col):
    elements = []
    #k =" "
    for i in range(row):
        elements.append([])
        for j in range(col):
            elements[i].append(EMPTY_UNCLICKED)
        #k=' '.join(map(str,elements[i]))
        #print(k.strip())
    return elements
#print(emptyGrid(3,3))
tet.testEmptyGrid()