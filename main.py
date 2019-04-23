from gui import *
from maze import *
from ia import *


def main():
    global canvas
    canvas = affichetk()
    #Maze = ["+--+-----+---------+","|  |     |         |","|  +  +  |  +  +   |","|     |  +  |  |   |","|     |     |  |   |","|  +--+--+--+  |   |","|  |     |  +--+   |","|  +  +  |         |","|     |  |  +------+","+-----+  |  |      |","|        |  |   +  |","|  +-----+  +   |  |","|  |            |  |","|  |  +---------+  |","|  |            |  |","|  |  +-----+---+  |","|  |        |      |","|  +-----+  +------+","|        |         |","+--------+---------+]"]
    #Maze = mazeborder(10,10)
    

def affichetk():
    window = tkinter.Tk()
    
    MenuBar = tkinter.Menu(window)
    M1 = tkinter.Menu(MenuBar, tearoff=0)
    M1.add_command(label="Crée", command=Test)
    M1.add_command(label="Résoudre", command=print(11))
    M1.add_separator() 
    M1.add_command(label="Importer", command=ImportFile)
    M1.add_command(label="Exporter", command=ExportFile)
    M1.add_separator()
    M1.add_command(label="Quitter", command=window.destroy)

    M2 = tkinter.Menu(MenuBar, tearoff=0)
    M2.add_command(label="Tournoi", command=print(10))
    M2.add_separator() 
    M2.add_command(label="Droite", command=print(10))
    M2.add_command(label="A*", command=print(10))
    M2.add_command(label="Djisktra", command=print(10))

    M3 = tkinter.Menu(MenuBar, tearoff=0)
    M3.add_command(label="Pacman", command=print(10))
    M3.add_command(label="Marble", command=print(10))
    
    MenuBar.add_cascade(label="Labyrinthe", menu=M1)
    MenuBar.add_cascade(label="IA", menu=M2)
    MenuBar.add_cascade(label="Jeu", menu=M3)
    
    window.config(menu=MenuBar)
    
    canvas = tkinter.Canvas(window, width=1000, height=1000, background='white')
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

def Test():
    fenetre = tkinter.Tk()

    global ScaleX
    global ScaleY
    
    frame1 = tkinter.Frame(fenetre)
    frame2 = tkinter.Frame(fenetre)
    frame3 = tkinter.Frame(fenetre)
    
    
    ScaleX = tkinter.Scale(frame1,orient="horizontal",from_=5, to=100,length=350,label='Taille (x)',tickinterval=10)
    ScaleX.pack()
    ScaleY = tkinter.Scale(frame1,orient="horizontal",from_=5, to=100,length=350,label='Taille (y)',tickinterval=10)
    ScaleY.pack()

    #List = tkinter.Listbox(frame2)
    #List.pack(side="left")
    #List.insert(0,"Backtracking")
    
    Check = tkinter.Checkbutton(frame2, text="Parfait?").pack(anchor = "e")

    Comfirm = tkinter.Button(frame3, text="Crée", command=Mazetk).pack(side="left",padx=10)
    Close = tkinter.Button(frame3, text="Fermer", command=fenetre.destroy).pack(side="right",padx=10)

    frame1.pack()
    frame2.pack()
    frame3.pack()


    
def Mazetk():
    x = ScaleX.get()
    y = ScaleY.get()
    canvas.delete("all")
    Maze = generatemaze(1,1,x,y)
    showmaze(Maze)
    showmazetk(canvas,Maze)


main()


