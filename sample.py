import battleship_tests as test
import random
import tkinter as tk
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
    return grid
    print(count)
def makeModel(data):
    data["number_of_rows"]=10
    data["number_of_cols"]=10
    data["board_size"]=500
    data["cell_size"] = data["board_size"]/(data["number_of_rows"])
    data["num_ships"]=5
    data["computer_board"]= emptyGrid(data["number_of_rows"],data["number_of_cols"])
    data["user_board"]=emptyGrid(data["number_of_rows"],data["number_of_cols"])
    data["computer_board"]=addShips(data["computer_board"],data["num_ships"]) 
    return data
def drawGrid(data, canvas, grid):
    for rows in range(0,10):
        for cols in range(0,10):
            if(grid[rows][cols]!=SHIP_UNCLICKED):
                canvas.create_rectangle(cols*data["cell_size"],rows*data["cell_size"],(cols+1)*data["cell_size"],(rows+1)*data["cell_size"],fill="blue")
            else:
                canvas.create_rectangle(cols*data["cell_size"],rows*data["cell_size"],(cols+1)*data["cell_size"],(rows+1)*data["cell_size"],fill="yellow")
    return
root=tk.Tk()
canvas=tk.Canvas(root,height=600,width=600)
canvas.pack()
grid=emptyGrid(10,10)
data=makeModel({ })
drawGrid(data,canvas,grid)
#grid=emptyGrid(10,10)
#test.testEmptyGrid()
#ship=createShip()
#checkShip(grid,ship)
#grid1=addShips(grid,2)
