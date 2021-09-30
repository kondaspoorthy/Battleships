"""
Battleship Project
Name: spoorthy
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
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


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,compCanvas,data["computer_board"],True)
    drawGrid(data,userCanvas,data["user_board"],True)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(row, col):
    grid=[]
    for i in range(row):
        grid.append([])
        for j in range(col):
            grid[i].append(EMPTY_UNCLICKED)
    return grid
#print(emptyGrid(3,3))
#test.testEmptyGrid()  

'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row=random.randint(1,8)
    col=random.randint(1,8)
    k=random.randint(0,1)
    if k==0:
        ship=[[row-1,col],[row,col],[row+1,col]]
    if k==1:
        ship=[[row,col-1],[row,col],[row,col+1]]
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in range(0,3):
        if grid[ship[i][0]][ship[i][1]]==EMPTY_UNCLICKED:
            continue
        else:
            return False
    return True

'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    num=0
    while(num<numShips):
        ship=createShip()
        result=checkShip(grid,ship)
        if(result==True):
            for i in range(0,3):
                grid[ship[i][0]][ship[i][1]]=SHIP_UNCLICKED
            num = num + 1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for rows in range(0,data["number_of_rows"]):
        for cols in range(0,data["number_of_cols"]):
            if(grid[rows][cols]!=SHIP_UNCLICKED):
                canvas.create_rectangle(cols*data["cell_size"],rows*data["cell_size"],(cols+1)*data["cell_size"],(rows+1)*data["cell_size"],fill="blue")
            else:
                canvas.create_rectangle(cols*data["cell_size"],rows*data["cell_size"],(cols+1)*data["cell_size"],(rows+1)*data["cell_size"],fill="yellow")
    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    count=0
    if(ship[0][1]==ship[1][1]==ship[2][1]):
        if(abs(ship[0][0]-ship[1][0])==1):
            count+=1
        if(abs(ship[1][0]-ship[2][0])==1):
            count+=1
        if(abs(ship[2][0]-ship[0][0])==1):
            count+=1
        if(count==2):
            return True
    return False
    


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    count=0
    if(ship[0][0]==ship[1][0]==ship[2][0]):
        if(abs(ship[0][1]-ship[1][1])==1):
            count+=1
        if(abs(ship[1][1]-ship[2][1])==1):
            count+=1
        if(abs(ship[2][1]-ship[0][1])==1):
            count+=1
        if(count==2):
            return True
    return False
'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    lst=[]
    for row in range(data["number_of_rows"]):
        for col in range(data["number_of_cols"]):
            if(row*data["cell_size"]<=event.y<=(row+1)*data["cell_size"] and col*data["cell_size"]<=event.x<=(col+1)*data["cell_size"] ):
                lst.append(row)
                lst.append(col)
    return lst


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    return


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
#test.testEmptyGrid()
    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
    #test.testEmptyGrid()
    #test.testCreateShip()
    #test.testCheckShip()
    #test.testAddShips()
    #test.testMakeModel()
    #test.testIsVertical()
    #test.testIsHorizontal()
    test.testGetClickedCell()