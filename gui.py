from tkinter import filedialog
import tkinter

def showmaze(Maze):
    print("\n".join(Maze))
	
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
            if Maze[i][j] == "─":
                canvas.create_line(minimum+ratiowidth*(j-0.5),minimum+ratioheight*i,minimum+ratiowidth*(j+0.5),minimum+ratioheight*i)
            elif Maze[i][j] == "│":
                canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*(i-0.5),minimum+ratiowidth*j,minimum+ratioheight*(i+0.5))
            elif Maze[i][j] == "┼" or Maze[i][j] == "┘" or Maze[i][j] == "┐" or Maze[i][j] == "┬" or Maze[i][j] == "┴" or Maze[i][j] == "├" or Maze[i][j] == "┤" or Maze[i][j] == "┌" or Maze[i][j] == "└":
                #create_circle(minimum+ratiowidth*j,minimum+ratioheight*i,3,canvas)
                pos = Plus(Maze,j,i)
                if pos[0] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*(j-0.5),minimum+ratioheight*i)
                if pos[1] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*(j+0.5),minimum+ratioheight*i)
                if pos[2] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*j,minimum+ratioheight*(i-0.5))
                if pos[3] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*j,minimum+ratioheight*(i+0.5))
            elif Maze[i][j] == "1":
                canvas.create_rectangle(minimum+ratiowidth*(j-0.9),minimum+ratioheight*(i-0.9),minimum+ratiowidth*(j+0.9),minimum+ratioheight*(i+0.9),fill="#000fff000")
            elif Maze[i][j] == "2":
                canvas.create_rectangle(minimum+ratiowidth*(j-0.9),minimum+ratioheight*(i-0.9),minimum+ratiowidth*(j+0.9),minimum+ratioheight*(i+0.9),fill="red")
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
        if list(Maze[y])[x-1] == "-" or list(Maze[y])[x-1] == "+" or list(Maze[y])[x-1] == "─":
            pos = ["G",0,0,0]
    if x != w-1:
        if list(Maze[y])[x+1] == "-" or list(Maze[y])[x+1] == "+" or list(Maze[y])[x+1] == "─":
            pos[1] = "D"
    if y != 0:
        if list(Maze[y-1])[x] == "|" or list(Maze[y-1])[x] == "+" or list(Maze[y-1])[x] == "│":
            pos[2] = "H"
    if y != h-1:
        if list(Maze[y+1])[x] == "|" or list(Maze[y+1])[x] == "+" or list(Maze[y+1])[x] == "│":
            pos[3] = "B"
    return pos

def ExportFile():
    f=tkinter.filedialog.asksaveasfile(
    title="Enregistrer le labyrinthe",
    filetypes=[('MAZE files','.maze')])
    print(f.name)

def ImportFile():
    f=tkinter.filedialog.askopenfilename(
    title="Ouvrir une labyrinthe",
    filetypes=[('MAZE files','.maze')])
    print(f.name)
    
