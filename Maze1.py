import tkinter as tkr
def main():
    canvas = affichetk()
    Maze = ["+--+-----+---------+",
            "|  |     |         |",
            "|  |  +  |  +  +   |",
            "|  +  |  +  |  |   |",
            "|     |     |  |   |",
            "|  +--+--+--+  |   |",
            "|  |     |  +--+   |",
            "|  +  +  |         |",
            "|     |  |  +------+",
            "+-----+  |  |      |",
            "|        |  |   +  |",
            "|  +-----+  +   |  |",
            "|  |            |  |",
            "|  |  +---------+  |",
            "|  |            |  |",
            "|  |  +-----+---+  |",
            "|  |        |      |",
            "|  +-----+  +------+",
            "|        |         |",
            "+--------+---------+]"]
    showmaze(Maze)
    showmazetk(canvas,Maze)
    tkr.mainloop()

def mazeborder(width,height):
    Maze = [['.'] * width for _ in range(height)]
    for i in range(height):
        if i == 0 or i == height-1:
            Maze[i]="".join(["+","-"*(width-2),"+"])
        else:
            Maze[i]="".join(["|"," "*(width-2),"|"])
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
                pos = Plus(Maze,j,i,width,height)
                if pos[0] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*(j-0.5),minimum+ratioheight*i)
                if pos[1] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*(j+0.5),minimum+ratioheight*i)
                if pos[2] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*j,minimum+ratioheight*(i-0.5))
                if pos[3] != 0:
                    canvas.create_line(minimum+ratiowidth*j,minimum+ratioheight*i,minimum+ratiowidth*j,minimum+ratioheight*(i+0.5))
        Maze[i] = "".join(Maze[i])
        
def create_circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill='black')

def Plus(Maze,x,y,w,h):
    pos = [0,0,0,0]
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

def generatemaze(nbr):
    #|version|
    # 1|width|height|1-,2 ,3|,4+.*width|*height
    1+1
    
def convertecode():
    v = int(input("Qu'elle version?"))
    if v == 1:
        w=int(input("Largeur?"))
        h=int(input("Hauteur?"))
        val = []
        for i in range(h):
            val.append(input(i+1))
            for ligne in range(len(val)):
                print(str(ligne+1)+val[ligne])
main()

