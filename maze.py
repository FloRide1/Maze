from random import *
from gui import *

def backtracking(x,y,w,h):      #retourne le labyrinthe sous forme d'un tableau de string                #
    Maze = mazeborder(w,h)
    temp = list(Maze[y])
    temp[x] = "0"
    OldPos = []
    Maze[y] = "".join(temp)
    while not(Finish(Maze)):
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
                temp[x+ax] = "?"
                Maze[y+ay] = "".join(temp)
            else :
                temp = list(Maze[y])
                temp[x] = "0"
                Maze[y] = "".join(temp)
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
                    del OldPos[-1]
                else :
                    end = True
            else :
                end = True

    Maze = Adapt(Maze)
    temp = list(Maze[1])
    temp[1] = "1"
    Maze[1] = "".join(temp)
    temp = list(Maze[h*2-1])
    temp[w*2-1] = "2"
    Maze[h*2-1] = "".join(temp)
    return Maze

def mazeborder(width,height):                 #retourne une grille de travail pour pouvoir créer le labyrinthe          
    Maze = [[] * width for _ in range(height*2+1)]
    for i in range(height*2+1):
        if i % 2 ==  0:
            Maze[i]="".join(["+","-+" * (width)])
        else:
            Maze[i]="".join(["|"," |" * (width)])
    return Maze

def Visit(Maze,x,y):                        # retourne untableau de 4 caractères qui permet de savoir quelles cases adjacentes ont été visitées (utilisé dans backtracking)
    h = len(Maze)
    w = len(Maze[0])
    pos = [0,0,0,0]
    if x != 1:
        if list(Maze[y])[x-2] == " ":
            pos = ["G",0,0,0]
    if x != w-2:
        if list(Maze[y])[x+2] == " ":
            pos[1] = "D"
    if y != 1:
        if list(Maze[y-2])[x] == " ":
            pos[2] = "H"
    if y != h-2:
        if list(Maze[y+2])[x] == " ":
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

def Finish(Maze):                           
    Result = True
    for i in Maze:
        if " " in i:
            Result = False
    return Result

def Adapt(Maze):                # recrée un labyrinthe sous forme d'un tableau de string plus adapté à l'affichage dans une console
    for y in range(len(Maze)):
        if "?" in Maze[y]:
            Maze[y] = " ".join((Maze[y]).split("?"))
        if "0" in Maze[y]:
            Maze[y] = " ".join((Maze[y]).split("0"))
        if "|" in Maze[y]:
            Maze[y] = "│".join((Maze[y]).split("|"))
        if "-" in Maze[y]:
            Maze[y] = "─".join((Maze[y]).split("-"))
        while "+" in Maze[y]:
            x = Maze[y].index("+")
            Result = Plus(Maze,x,y)
            if Result == ["G",0,0,0]:
                Style = "─"
            elif Result == [0,"D",0,0]:
                Style = "─"
            elif Result == [0,0,"H",0]:
                Style = "│"
            elif Result == [0,0,0,"B"]:
                Style = "│"
            elif Result == ["G","D",0,0]:
                Style = "─"
            elif Result == [0,0,"H","B"]:
                Style = "│"
            elif Result == ["G",0,"H",0]:
                Style = "┘"
            elif Result == ["G",0,0,"B"]:
                Style = "┐"
            elif Result == [0,"D","H",0]:
                Style = "└"
            elif Result == [0,"D",0,"B"]:
                Style = "┌"
            elif Result == ["G",0,"H","B"]:
                Style = "┤"
            elif Result == [0,"D","H","B"]:
                Style = "├"
            elif Result == ["G","D","H",0]:
                Style = "┴"
            elif Result == ["G","D",0,"B"]:
                Style = "┬"
            else :
                Style = "┼"
            temp = list(Maze[y])
            temp[x] = Style
            Maze[y] = "".join(temp)
    return Maze

def Fusion(w,h):                                # algorithme de création d'un labyrinthe par fusion pas utilisé dans le programme
    Maze = mazeborder(w,h)
    nbr = 0
    for i in range(h):
        temp = list(Maze[2*i+1])     
        for j in range(w):
            temp[2*j+1] = str(nbr)
            nbr += 1
        Maze[2*i] = list(Maze[2*i])
        Maze[2*i+1] = temp
    
    while not(MazeFinish(Maze,w,h)):
        Alx = randint(1,2*w-2)
        Aly = randint(1,2*h-2)
        wall = Maze[Aly][Alx]
        print("X : ",Alx," Y : ",Aly, " Wall : ",wall)
        if wall == "-":
            Hover = Maze[Aly-1][Alx]
            Botom = Maze[Aly+1][Alx]
            print("Wall : ",wall," Hover : ",Hover," Bottom : ",Botom)
            if Hover != Botom:
                Maze[Aly][Alx] = " "
                if Hover < Botom:
                    Maze = Transform(Maze,Botom,Hover)
                else:
                    Maze = Transform(Maze,Hover,Botom)
            #print(showmaze(Adapt(FusionAdapt(Maze))))
        elif wall == "|":
            Rigt = Maze[Aly][Alx+1]
            Left = Maze[Aly][Alx-1]
            print("Wall : ",wall," Right : ",Rigt," Left : ",Left)
            if Rigt != Left:
                Maze[Aly][Alx] = " "
                if Rigt < Left:
                    Maze = Transform(Maze,Left,Rigt)
                else:
                    Maze = Transform(Maze,Rigt,Left)
            #print(showmaze(Adapt(FusionAdapt(Maze))))
    Maze = FusionAdapt(Maze)
    Maze = Adapt(Maze)
    return Maze

def Transform(Maz,Last,New):                        #utilisé dans fusion (pas utilisé dans le programme)
    Maze = Maz
    for i in range(len(Maze)):
        for j in range(Maze[i].count(Last)):
            Maze[i][Maze[i].index(Last)] = New
    return Maze

def MazeFinish(Maze,w,h):                           #pas utilisé dans le programme
    Finish = True
    nbr = w
    for i in range(h):
        if Maze[2*i+1].count("0") != nbr:
              Finish = False
              if Maze[2*i+1].count("0") == 9 and 2*i+1==19 :
                  print(showmaze(Adapt(FusionAdapt(Maze))))
              print("Nbr de 0 :",Maze[2*i+1].count("0")," y : ",2*i+1)
    return Finish

def FusionAdapt(Maz):                               #pas utilisé dans le programme
    Maze = Maz
    for i in range(len(Maze)):
        Maze[i] = "".join(Maze[i])
    return Maze

#Fusion(10,10)
