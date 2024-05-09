
import pygame as p, math,random as r
p.init()

def makeWindow():
    global window
    global board
    window = p.display.set_mode([300, 300])
    window.fill((255, 255, 255))
    board = [
        ["*","*","*"],
        ["*","*","*"],
        ["*","*","*"]]
    
def drawBoard():
    global window
    p.draw.line(window, (0,0,0), (5,100), (297,100), 4)
    p.draw.line(window, (0,0,0), (3,200), (294,200), 4)
    p.draw.line(window, (0,0,0), (100,4), (100,298), 4)
    p.draw.line(window, (0,0,0), (200,6), (200,294), 4)
    ### The Rest of the board
    global board
    for X in range(3):
        for Y in range(3):
            item = board[Y][X]
            if item == "*":
                pass
            elif item == "X":
                p.draw.line(window, (255,0,0), (   (X*100)+10, (Y*100)+10    ) , (   (X*100)+90, (Y*100)+90    ), 10)
                p.draw.line(window, (255,0,0), (   (X*100)+90, (Y*100)+10    ) , (   (X*100)+10, (Y*100)+90    ), 10)
            elif item == "O":
                p.draw.circle(window, (0,0,255), ((X*100)+50,(Y*100)+50), 40, 10)
                
def find():
    global board
    global turn
    turn = False
    x,y = p.mouse.get_pos()
    x,y = math.ceil(x/100),math.ceil(y/100)
    if board[int(y-1)][int(x-1)] == "*":
        board[int(y-1)][int(x-1)] = "X"

def runCPU():
    global board
    global turn
    num1,num2 = r.randint(0,2),r.randint(0,2)
    while board[num1][num2] == "X" or board[num1][num2] == "O":
        num1,num2 = r.randint(0,2),r.randint(0,2)
    board[num1][num2] = "O"
    turn = True
    
def checkWin():
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":return True, "X"
    if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":return True, "X"
    if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":return True, "X"
    

turn = True
makeWindow()
while True:
    for event in p.event.get():
        if event.type == p.MOUSEBUTTONDOWN and turn == True:
            find()
            turn = False
    drawBoard()
    p.display.flip()
    if turn == False:
        runCPU()
        turn = True
