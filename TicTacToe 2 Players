moves, col, row = 0, 3, 3
player = ' '
LINE_CLEAR = '\x1b[2K'
LINE_UP = '\033[1A'

grid = [[player for i in range(col)] for j in range(row)]
import time

def terminal(movest):
    final = ''
    if movest == 9:
        final = 'draw'
    for row in range(3):
        col = 0
        if grid[row][col] == 'x':
            if grid[row][col + 1] == grid[row][col + 2] == 'x':
                final = 'xwin'
        if grid[row][col] == 'o':
            if grid[row][col + 1] == grid[row][col + 2] == 'o':
                final = 'owin'
    if final != 'owin' or final != 'xwin':
        for col in range(3):
            row = 0
            if grid[row][col] == 'x':
                if grid[row + 1][col] == grid[row + 2][col] == 'x':
                    final = 'xwin'
            if grid[row][col] == 'o':
                if grid[row + 1][col] == grid[row + 2][col] == 'o':
                    final = 'owin'
    if final != 'owin' or final != 'xwin':
        if grid[1][1] == 'x':
            if grid[0][0] == grid[2][2] == 'x':
                final = 'xwin'
            elif grid[0][2] == grid[2][0] == 'x':
                final = 'xwin'
        if grid[1][1] == 'o':
            if grid[0][0] == grid[2][2] == 'o':
                final = 'owin'
            elif grid[0][2] == grid[2][0] == 'o':
                final = 'owin'
    return final

def lineupnclear(num):
    x = 0
    while x < num:
        print(LINE_UP, end = LINE_CLEAR)
        x += 1

def printstate():
    for row in grid:
        dft = str(row)
        dft = dft.replace(',', ' |')
        dft = dft.replace('[', ' ')
        dft = dft.replace("'", '')
        row = dft.replace(']', ' ')
        print(row)
        print('-----------')
    print(LINE_UP, end = LINE_CLEAR)

def takeinput(playerti):    
    posti = input('row,col: ')
    if int(posti[:1]) > 3 or int(posti[-1:]) < 1 or posti[1:2] != ',' :
        lineupnclear(6)
        print('InValid Syntax, Retry')
        time.sleep(2)
        lineupnclear(1)
        printstate()
        posti = input('row,col: ')
    if grid[int(posti[:1]) - 1][int(posti[-1:]) - 1] == 'x' or grid[int(posti[:1]) - 1][int(posti[-1:]) - 1] == 'o':
        lineupnclear(6)
        print("Choose another block")
        lineupnclear(1)
        time.sleep(2)
        printstate()
        posti = input('row,col: ')
    position(posti, playerti)

def playerselect(movesps, playerps):
    if movesps == 0:
        playerps = 'x'
    elif movesps > 0 and playerps == 'x':
        playerps = 'o'
    elif playerps == 'o':
        playerps = 'x'
    return playerps
  
def position(pos, playerp):
    grid[int(pos[:1]) - 1][int(pos[-1:]) - 1] = playerp
    

play = input('Do you want to play Tic Tac Toe? (Y/N) ')
if play.lower() == 'n':
    print('Bye, see you soon')
elif play.lower() == 'y':
    lineupnclear(2)
    
    while terminal(moves) != 'xwin' and terminal(moves) != 'owin' and terminal(moves) != 'draw':
        printstate()
        player = playerselect(moves,player)
        takeinput(player)
        moves += 1
        lineupnclear(6)
else:
    print('Wrong Input')

if terminal(moves) == 'draw':
    printstate()
    print('Its a DRAW')
elif terminal(moves) == 'xwin':
    printstate()
    print('X WINS THIS GAME')
elif terminal(moves) == 'owin':
    printstate()
    print('O WINS THIS GAME')
