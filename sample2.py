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
    
ship =[[row,col],[row,col],[row,col]]
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