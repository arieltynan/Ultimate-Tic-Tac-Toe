#importing Packages from tkinter
from tkinter import * 
from tkinter import messagebox
 
Player1 = "X"
endGame = False
turnCount = 0
winner = ""


def clicked(r,c):

    #player
    global Player1
    global turnCount

    turnCount += 1
    b[r][c].config(state=DISABLED)
    b[r][c].config(text = Player1)
    states[r][c] = Player1

    checkWinMinor()
    setBoard(r,c)

    if Player1 == 'X':
        Player1 = 'O'
    elif Player1 == 'O':
        Player1 = 'X'
    #print(states)

def setBoard(r,c):
    global board #what board next turn is active in
    if (r == 0 or r == 3 or r == 6) and (c == 0 or c == 3 or c == 6):
        board = 0
    if (r == 0 or r == 3 or r == 6) and (c == 1 or c == 4 or c == 7):
        board = 1
    if (r == 0 or r == 3 or r == 6) and (c == 2 or c == 5 or c == 8):
        board = 2
    if (r == 1 or r == 4 or r == 7) and (c == 0 or c == 3 or c == 6):
        board = 3
    if (r == 1 or r == 4 or r == 7) and (c == 1 or c == 4 or c == 7):
        board = 4
    if (r == 1 or r == 4 or r == 7) and (c == 2 or c == 5 or c == 8):
        board = 5
    if (r == 2 or r == 5 or r == 8) and (c == 0 or c == 1 or c == 2):
        board = 6
    if (r == 2 or r == 5 or r == 8) and (c == 1 or c == 4 or c == 7):
        board = 7
    if (r == 2 or r == 5 or r == 8) and (c == 2 or c == 5 or c == 8):
        board = 8
    reconfigure(board)


def reconfigure(board):
    valids = [] #label for valid indexes in ttt board used for next turn
    if board == 0:
        valids = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    elif board == 1:
        valids = [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]]
    elif board == 2:
        valids = [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]]
    elif board == 3:
        valids = [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]]
    elif board == 4:
        valids = [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]
    elif board == 5:
        valids = [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]]
    elif board == 6:
        valids = [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]]
    elif board == 7:
        valids = [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]]
    elif board == 8:
        valids = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]

    for i in range(9):
        for j in range(9):
            b[i][j].config(state=DISABLED)
    for i in range(9):
        for j in range(9):
            index = [i,j]
            if index in valids and states[i][j] == 0:
                b[i][j].config(state=NORMAL)


def checkWinMinor():
    global endGame
    global winner
    if states[0][0] == states[1][1] == states[2][2] != 0 or states[0][2] == states[1][1] == states[2][0] != 0:
        print(f"Game is over, {Player1} wins!")
        endGame = True
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0 or states[0][i] == states[1][i] == states[2][i] != 0:
            print(f"Game is over, {Player1} wins!")
            endGame = True

    if endGame == True:
        for i in range(3):
            for j in range(3):
                b[i][j].config(state=DISABLED)
    #elif turnCount == 9:
    #    print("No one wins")
 
# Design window
#Creating the Canvas
root = Tk()
# Title of the window            
root.title("Ultimate TicTacToe") 
root.resizable(0,0)
 
#Button
b = [
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]]

mb = []
 
#text for buttons
states = [
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]]

for i in range(9):
    for j in range(9):
                                        
        b[i][j] = Button(
                        height = 1, width = 2,
                        font = ("Helvetica","20"),
                        command = lambda r = i, c = j : clicked(r,c),
                        activebackground= 'blue'
                        )
        b[i][j].grid(row = i, column = j)

    
 
mainloop()           