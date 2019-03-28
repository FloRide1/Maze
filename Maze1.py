import tkinter as tkr
from random import *
def main():
    canvas = affichetk()
    #Maze = ["+--+-----+---------+","|  |     |         |","|  +  +  |  +  +   |","|     |  +  |  |   |","|     |     |  |   |","|  +--+--+--+  |   |","|  |     |  +--+   |","|  +  +  |         |","|     |  |  +------+","+-----+  |  |      |","|        |  |   +  |","|  +-----+  +   |  |","|  |            |  |","|  |  +---------+  |","|  |            |  |","|  |  +-----+---+  |","|  |        |      |","|  +-----+  +------+","|        |         |","+--------+---------+]"]
    Maze = mazeborder(100,100)
    Maze = generatemaze(1,1,Maze)
    showmaze(Maze)
    showmazetk(canvas,Maze)
    tkr.mainloop()

def mazeborder(width,height):
    if width%2 != 1:
        width+=1
    if height%2 != 1:
        height+=1
    Maze = [['.'] * width for _ in range(height)]
    for i in range(height):
        if i %2 ==  0:
            Maze[i]="".join(["+","-+"*(int((width-2)/2))])
        else:
            Maze[i]="".join(["|"," |"*(int((width-2)/2))])
    return Maze

def showmaze(Maze):
    print("\n".join(Maze))

def affichetk():
    window = tkr.Tk()
    canvas = tkr.Canvas(window, width=1000, height=1000, background='white')
    canvas.grid()
    
    
    #Bordure
    minimum = 10
    maximum = 990
    
    canvas.create_line(minimum,minimum,minimum,maximum)
    canvas.create_line(minimum,minimum,maximum,minimum)
    canvas.create_line(minimum,maximum,maximum,maximum)
    canvas.create_line(maximum,minimum,maximum,maximum)
    
    canvas.pack()
    
    return canvas


def showmazetk(canvas,Maze):
    minimum = 20
    maximum = 980
    height = len(Maze)
    width = len(Maze[0])
    ratiowidth = maximum/width
    ratioheight = maximum/height
    for i in range(height):
        Maze[i] = list(Maze[i])
        for j in range(width):
            if Maze[i][j] == "-":
                canvas.create_line(minimum+ratiowidth*(j-0.5),minimum+ratioheight*i,minimum+ratiowidth*(j+0.5),minimum+ratioheight*i)
            elif Maze[i][j] == "|":
                canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*(i-0.5),minimum+ratiowidth*j,minimum+ratioheight*(i+0.5))
            elif Maze[i][j] == "+":
                create_circle(minimum+ratiowidth*j,minimum+ratioheight*i,3,canvas)
                pos = Plus(Maze,j,i)
                if pos[0] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*(j-0.5),minimum+ratioheight*i)
                if pos[1] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*(j+0.5),minimum+ratioheight*i)
                if pos[2] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*j,minimum+ratioheight*(i-0.5))
                if pos[3] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*j,minimum+ratioheight*(i+0.5))
            #elif Maze[i][j] == "0":
                #canvas.create_rectangle(minimum+ratiowidth*(j-0.9),minimum+ratioheight*(i-0.9),minimum+ratiowidth*(j+0.9),minimum+ratioheight*(i+0.9),fill="#000fff000")
            elif Maze[i][j] == ".":
                canvas.create_rectangle(minimum+ratiowidth*(j-0.75),minimum+ratioheight*(i-0.75),minimum+ratiowidth*(j+0.75),minimum+ratioheight*(i+0.75),fill="orange")
        Maze[i] = "".join(Maze[i])
        
def create_circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill='black')

def Plus(Maze,x,y):
    pos = [0,0,0,0]
    h = len(Maze)
    w = len(Maze[0])  
    if x != 0:
        if list(Maze[y])[x-1] == "-" or list(Maze[y])[x-1] == "+":
            pos = ["G",0,0,0]
    if x != w-1:
        if list(Maze[y])[x+1] == "-" or list(Maze[y])[x+1] == "+":
            pos[1] = "D"
    if y != 0:
        if list(Maze[y-1])[x] == "|" or list(Maze[y-1])[x] == "+":
            pos[2] = "H"
    if y != h-1:
        if list(Maze[y+1])[x] == "|" or list(Maze[y+1])[x] == "+":
            pos[3] = "B"
    return pos

def generatemaze(x,y,Maze):
    h = len(Maze)
    w = len(Maze[0])
    temp = list(Maze[y])
    temp[x] = "0"
    OldPos = []
    NbrAll = 1
    Maze[y] = "".join(temp)
    while NbrAll < (h/2)*(w/2)-1:
        end = False
        while not(end) :
            Result = ChangePos(Maze,x,y)
            if len(Result) != 1:
                OldPos.append([x,y])
                x = Result[0]
                y = Result[1]
                if list(Maze[y])[x] == " ":
                    temp = list(Maze[y])
                    temp[x] = "."
                    Maze[y] = "".join(temp)
                ax = Result[2]
                ay = Result[3]
                temp = list(Maze[y+ay])
                temp[x+ax] = " "
                Maze[y+ay] = "".join(temp)
            else :
                temp = list(Maze[y])
                temp[x] = "0"
                Maze[y] = "".join(temp)
                NbrAll += 1
                end = True
        end = False
        while not(end):
            if len(OldPos)-1 != 0:
                Pos = OldPos[len(OldPos)-1]
                x = Pos[0]
                y = Pos[1]
                if len(ChangePos(Maze,x,y)) == 1:
                    temp = list(Maze[y])
                    temp[x] = "0"
                    Maze[y] = "".join(temp)
                    NbrAll += 1
                    del OldPos[-1]
                else :
                    end = True
            else :
                end = True
    print(NbrAll)
    return Maze
    
def Visit(Maze,x,y):
    h = len(Maze)
    w = len(Maze[0])
    pos = [0,0,0,0]
    if x != 1:
        if list(Maze[y])[x-2] != "." and list(Maze[y])[x-2] != "0":
            pos = ["G",0,0,0]
    if x != w-2:
        if list(Maze[y])[x+2] != "." and list(Maze[y])[x+2] != "0":
            pos[1] = "D"
    if y != 1:
        if list(Maze[y-2])[x] != "." and list(Maze[y-2])[x] != "0":
            pos[2] = "H"
    if y != h-2:
        if list(Maze[y+2])[x] != "." and list(Maze[y+2])[x] != "0":
            pos[3] = "B"
    return pos

def ChangePos(Maze,x,y):
    Posib = Visit(Maze,x,y)
    while 0 in Posib:
        Posib.remove(0)
    if len(Posib)==0:
        Result = [0]
    else:
        Posib = choice(Posib)   
        if Posib == "B":
            Result = [x,y+2,0,-1]
        elif Posib == "G":
            Result = [x-2,y,1,0]
        elif Posib == "D":
            Result = [x+2,y,-1,0]
        elif Posib == "H":
            Result = [x,y-2,0,1]
    return Result

    
    
main()

