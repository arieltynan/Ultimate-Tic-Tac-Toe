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

    checkWin()

    
    if Player1 == 'X':
        Player1 = 'O'
 
     
    elif Player1 == 'O':
        Player1 = 'X'
    #print(states)

def checkWin():
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
    elif turnCount == 9:
        print("No one wins")

# Design window
#Creating the Canvas
root = Tk()
# Title of the window            
root.title("Ultimate TicTacToe") 
root.resizable(0,0)
 
#Button
b = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]
 
#text for buttons
states = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]
 
for i in range(3):
    for j in range(3):
                                          
        b[i][j] = Button(
                        height = 4, width = 8,
                        font = ("Helvetica","20"),
                        command = lambda r = i, c = j : clicked(r,c),
                        activebackground= 'blue'
                        )
        b[i][j].grid(row = i, column = j)
 
 
mainloop()           