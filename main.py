from gui import *
from maze import *
def main():
    canvas = affichetk()
    #Maze = ["+--+-----+---------+","|  |     |         |","|  +  +  |  +  +   |","|     |  +  |  |   |","|     |     |  |   |","|  +--+--+--+  |   |","|  |     |  +--+   |","|  +  +  |         |","|     |  |  +------+","+-----+  |  |      |","|        |  |   +  |","|  +-----+  +   |  |","|  |            |  |","|  |  +---------+  |","|  |            |  |","|  |  +-----+---+  |","|  |        |      |","|  +-----+  +------+","|        |         |","+--------+---------+]"]
    Maze = generatemaze(1,1,10,10)
    #Maze = mazeborder(10,10)
    showmaze(Maze)
    showmazetk(canvas,Maze)
    tkr.mainloop()

main()

