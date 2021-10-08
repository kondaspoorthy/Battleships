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
canvas=tk.Canvas(root,width=500,height=500)
canvas.pack()
drawGrid({ })

lst=[[2,3],[4,5],[9,8]]
lst[1][0]