#Non-GUI TicTacToe

import pandas as pd 
class Square:
    def ___init___(self, grid, state):
        #grid-array of 3x3 grid
        #state- Open, X/O win, or draw
        self.grid = grid
        self.state = state
      
def playMove(player): #Player 1-2, space 1-9
    if player == 1:
        return 1
    else:
        return -1

def newGame():
    game = Square() #init new 3x3 square
    game.grid = [0,0,0,0,0,0,0,0,0]
    #X = 1, O = -1
    game.state = 0
    #Open = 0, XWin = 1, OWin = -1, Draw = 2
    return game

def checkWin(arr):
    if arr[0] == arr[1] == arr[2] != 0 or \
        arr[3] == arr[4] == arr[5] != 0 or \
        arr[6] == arr[7] == arr[8] != 0 or \
        arr[0] == arr[3] == arr[6] != 0 or \
        arr[1] == arr[4] == arr[7] != 0 or \
        arr[2] == arr[5] == arr[8] != 0 or \
        arr[0] == arr[4] == arr[8] != 0 or \
        arr[2] == arr[4] == arr[6] != 0:
        if player == 1:
            print("Player 1, (X's) Won!")
            return 1
        else:
            print("Player 2, (O's) Won!")
            return -1

    if 0 not in game.grid:
        print("Everyone Loses! Yayyy")
        return 2
    else:
        return 0

def printGrid(vis):
    disp = [] #grid display array
    for i in range(0,9):
        if vis[i] == 1:
            disp.append("X")
        elif vis[i] == -1:
            disp.append("O")
        else:
            disp.append(" ")

    print(disp[0], "|", disp[1], "|", disp[2])
    print(disp[3], "|", disp[4], "|", disp[5])
    print(disp[6], "|", disp[7], "|", disp[8])

def checkMove(grid,p):
    move = int(input("Player " + str(p) + ", where do you want to go? (1-9):   "))
    while move > 9 or move < 0 or grid[int(move - 1)] != 0:
        move = int(input("Pick a valid space (1-9):   "))
    return move

## Run Program ##
game = newGame()
player = 1
while game.state == 0:
    printGrid(game.grid)
    move = checkMove(game.grid, player)
    game.grid[(move)-1] = playMove(int(player))
    game.state = checkWin(game.grid)
    if player == 1:
        player = 2
    else:
        player = 1

printGrid(game.grid)
