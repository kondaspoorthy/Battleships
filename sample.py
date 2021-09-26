import battleship_tests as test
import random
EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4
def emptyGrid(row, col):
    grid = []
    for i in range(row):
        grid.append([])
        for j in range(col):
            grid[i].append(EMPTY_UNCLICKED)
    return grid
def createShip():
    row=random.randint(1,8)
    col=random.randint(1,8)
    k=random.randint(0,1)
    if k==0:
        ship=[[row-1,col],[row,col],[row+1,col]]
    if k==1:
        ship=[[row,col-1],[row,col],[row,col+1]]
    return ship
def checkShip(grid, ship):
    for i in range(0,3):
        if grid[ship[i][0]][ship[i][1]]==EMPTY_UNCLICKED:
            continue
        else:
            return False
    return True
def addShips(grid, numShips):
    num=0
    count=0
    while(num<numShips):
        ship=createShip()
        s=checkShip(grid,ship)
        if(s==True):
            for i in range(0,3):
                grid[ship[i][0]][ship[i][1]]=SHIP_UNCLICKED
                count=count+1
            num = num + 1
    print(count)
    return grid
grid=emptyGrid(10,10)
ship=createShip()
checkShip(grid,ship)
addShips(grid,2)
