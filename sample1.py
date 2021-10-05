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
def drawGrid(data, canvas, grid, showShips):
    for rows in range(0,10):
        for cols in range(0,10):
            if(grid[rows][cols]!=SHIP_UNCLICKED):
                canvas.create_rectangle(cols*data["cell_size"],rows*data["cell_size"],(cols+1)*data["cell_size"],(rows+1)*data["cell_size"],fill="blue")
            else:
                canvas.create_rectangle(cols*data["cell_size"],rows*data["cell_size"],(cols+1)*data["cell_size"],(rows+1)*data["cell_size"],fill="yellow")
    return
root=tk.Tk()
def drawShip(data, canvas, ship):
    for i in range(0,3):
        canvas.create_rectangle(ship[i][1]*data["cell_size"],ship[i][0]*data["cell_size"],ship[i][1]*data["cell_size"]+data["cell_size"],ship[i][0]*data["cell_size"]+data["cell_size"],fill="white")    
    return
data["computer_board"]==SHIP_CLICKED or data["computer_board"]==EMPTY_CLICKED):
def runGameTurn(data, row, col):
    if(data["computer_board"]==SHIP_CLICKED or data["computer_board"]==EMPTY_CLICKED):
        return
    else:
        updateBoard(data,data["computer_board"],row,col,"user")
    choice=getComputerGuess(data["user_board"])
    updateBoard(data,data["user_board"],choice[0],choice[1],"comp")
    return


