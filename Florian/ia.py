def getGraph(Maze):
    h = len(Maze)
    w = len(Maze[0])
    PosX = 1
    PosY = 1
    Node = 1
    Distance = 0
    V = []
    S = [1]
    SPos = [[1,1]]
    P = [[]]
    A = []
    WaitList = []
    Deplacement = Movement(Maze,V,PosX,PosY)
    WaitList.append([[1],Deplacement])
    while len(WaitList) > 0:
        if len(Deplacement) == 1 and [PosX,PosY] != [w-2,h-2]:
            Distance += 1
            V.append([PosX,PosY])
            P[-1].append([PosX,PosY])
            Pos = Move(Deplacement[0],PosX,PosY)
            PosX = Pos[0]
            PosY = Pos[1]
        else:
            S.append(S[-1]+1)
            SPos.append([PosX,PosY])
            P[-1].append([PosX,PosY])
            A.append([Node,S[-1],Distance])
            V.append([PosX,PosY])
            P.append([])  
            if len(Deplacement) > 1 or ([PosX,PosY] == [w-2,h-2] and len(Deplacement) != 0):
                List = [S[-1]]
                List.append(Deplacement)
                WaitList.append(List)
            Distance = 1
            WaitList = RemoveList(WaitList)
            if len(WaitList) > 0:
                Node = WaitList[0][0]
                PosX = SPos[Node-1][0]
                PosY = SPos[Node-1][1]
                P[-1].append([PosX,PosY])
                Pos = Move(WaitList[0][1][0],PosX,PosY)
                PosX = Pos[0]
                PosY = Pos[1]
                P[-1].append([PosX,PosY])
        Deplacement = Movement(Maze,V,PosX,PosY)
    return [S,A,SPos,P]
        

def Movement(Maze,V,x,y):
    h = len(Maze)
    w = len(Maze[0])
    Pos = [0,0,0,0]
    if x != 1:
        if list(Maze[y])[x-1] == " " and not([x-1,y] in V):
            Pos = ["G",0,0,0]
    if x != w-2:
        if (list(Maze[y])[x+1] == " " or list(Maze[y])[x+1] == "2") and not([x+1,y] in V):
            Pos[1] = "D"
    if y != 1:
        if list(Maze[y-1])[x] == " " and not([x,y-1] in V):
            Pos[2] = "H"
    if y != h-2:
        if (list(Maze[y+1])[x] == " " or list(Maze[y+1])[x] == "2") and not([x,y+1] in V):
            Pos[3] = "B"
    while 0 in Pos:
        Pos.remove(0)
    return Pos

def Move(Movement,PosX,PosY):
    X = PosX
    Y = PosY
    if Movement == "G":
        X = PosX - 1
    elif Movement == "D":
        X = PosX + 1
    elif Movement == "H":
        Y = PosY - 1
    elif Movement == "B":
        Y = PosY + 1
    return [X,Y]

def RemoveList(WaitList):
    del WaitList[0][1][0]
    if len(WaitList[0][1]) == 0:
        del WaitList[0]
    return WaitList

def Djisktra(Maze):
    Graph = getGraph(Maze)
    S = Graph[0]
    A = Graph[1]
    Spos= Graph[2]
    P = Graph[3]
    h = len(Maze)
    w = len(Maze[0])
    ReS = [[] * 1 for _ in range(len(S))]
    #ReS = [[]]*len(S)
    ReS[0].append([0,1])
    Select = 1
    EnD = [1]
    Objective = Spos.index([w-2,h-2])+1
    Finish = False
    while not(Finish):
        Check = NodeConnection(Select,S,A,EnD)
        print("Select : ",Select,"EnD : ",EnD)
        print("ReS  : ",ReS)
        for i in range(len(Check)):
            Dist = ReS[Select-1][-1][0] + A[Check[i]-1][2]
            ReS[Check[i]].append([Dist,Select])
            print("ReSSA  : ",ReS)
        Possib = []
        for i in range(len(S)):
            if not(i+1 in EnD):
                for j in range(len(ReS[i])):
                    Possib.append(ReS[i][j])
        MIN = 100000000
        IND = 100000000
        for i in range(len(Possib)):
            if Possib[i][0] < MIN:
                IND = i
                MIN = Possib[i][0]
        print("MIN  : ",MIN," IND : ",IND," Possib : ",Possib)
        ReS[Possib[IND][1]-1].append(Possib[IND])
        print("ReSSB  : ",ReS)
        EnD.append(Possib[IND][1])
        Select = Possib[IND][1]
        if Select == Objective:
            Finish = True
    print("SALUTION : ",ReS)
    Sol = [Select]
    while Select != 1:
        Select = ReS[Select-1][-1][1]
        Sol.append(Select)
    print("Solution : ",Sol)
    
def NodeConnection(Select,S,A,EnD):
    Check = []
    for i in range(len(A)):
        if (A[i][0] == Select and not(A[i][1] in EnD)) or (A[i][1] == Select and not(A[i][0] in EnD)):
            if A[i][0] == Select:
                Check.append(A[i][1])
            else :
                Check.append(A[i][0])
    return Check


        
