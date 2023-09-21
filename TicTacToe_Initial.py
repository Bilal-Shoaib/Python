import time
import math
import copy
LINE_CLEAR = '\x1b[2K'
LINE_UP = '\033[1A'

board = [[' ']*3 for j in range(3)]

def lineupnclear(num):
    x = 0
    while x < num:
        print(LINE_UP, end = LINE_CLEAR)
        x += 1
#########################################

def printstate():
    for row in board:
        dft = str(row)
        dft = dft.replace(',', ' |')
        dft = dft.replace('[', ' ')
        dft = dft.replace("'", '')
        row = dft.replace(']', ' ')
        print(row)
        print('-----------')
    print(LINE_UP, end = LINE_CLEAR)
######################################

def takeinput():    
    posti = input('row,col: ')
    if int(posti[:1]) > 2 or int(posti[-1:]) < 0 or posti[1:2] != ',' :        
        lineupnclear(6)
        print('InValid Syntax, Retry')
        time.sleep(2)
        lineupnclear(1)
        printstate()
        posti = input('row,col: ')
    if board[int(posti[:1])][int(posti[-1:])] == 'x' or board[int(posti[:1])][int(posti[-1:])] == 'o':
        lineupnclear(6)
        print("Choose another block")
        lineupnclear(1)
        time.sleep(2)
        printstate()
        posti = input('row,col: ')
    return posti
#######################################################################################################

def minimax(boardm, playerm):
    if playerm == 'x':
        othrplayer = 'o'
        best = {'position':None, 'score':-math.inf}
    else:
        othrplayer = 'x'
        best = {'position':None, 'score':math.inf}
    if terminal(boardm):
        if utility(boardm) == 1:
            best['score'] = 1
            return best
        elif utility(boardm) == -1:
            best['score'] = -1
            return best
        else:
            best['score'] = 0
            return best
    for action in actions(boardm):
        dupe = results(boardm, action, playerm)
        sim_best = minimax(dupe, othrplayer)
        dupe = results(boardm, action, ' ')
        sim_best['position'] = action
        if playerm == 'x':
            if sim_best['score'] > best['score']:
                best = sim_best
        else:
            if sim_best['score'] < best['score']:
                best = sim_best
    return best
#######################################################
def plrselect(boardp):
    xmoves = 0
    omoves = 0
    empty = 0
    player = ''
    for row in range(3):
        for col in range(3):
            if boardp[row][col] == ' ':
                empty += 1
            elif boardp[row][col] == 'x':
                xmoves += 1
            elif boardp[row][col] == 'o':
                omoves += 1
    if empty == 9 and xmoves == 0:
        player = 'x'
    elif xmoves == omoves + 1:
        player = 'o'
    elif xmoves == omoves:
        player = 'x'
    return player
###########################################

def actions(boarda):
    empty = 0
    empty_spaces = []
    for row in range(3):
        for col in range(3):
            if boarda[row][col] == ' ':
                empty_spaces.append(f'{row},{col}')
                empty += 1
    return empty_spaces
#####################################################

def results(boardr, actionr, playerr):
    dupe = copy.deepcopy(boardr)
    row = int(actionr[:1])
    col = int(actionr[-1:])
    if (dupe[row][col] != 'x' and dupe[row][col] != 'o') or playerr == ' ':
        dupe[row][col] = playerr
        return dupe
    else:
        return boardr
############################################################################

def utility(boardu):
    if winner(boardu) == 'x':
        return 1
    elif winner(boardu) == 'o':
        return -1
    else:
        return 0    
    
###############################

def terminal(boardt):
    flag = False       
    empty = 0
    for row in range(3):
        for col in range(3):
            if boardt[row][col] == ' ':
                empty += 1
    if empty == 0:
        flag = True
    for row in range(3):
        col = 0
        if boardt[row][col] == boardt[row][col + 1] == boardt[row][col + 2] == 'x':
                flag = True
        if boardt[row][col] == boardt[row][col + 1] == boardt[row][col + 2] == 'o':
                flag = True
    if flag != True:
        for col in range(3):
            row = 0
            if boardt[row][col] == boardt[row + 1][col] == boardt[row + 2][col] == 'x':
                    flag = True
            if boardt[row][col] == boardt[row + 1][col] == boardt[row + 2][col] == 'o':
                    flag = True
    if flag != True:
        if boardt[1][1] == boardt[0][0] == boardt[2][2] == 'x':
                flag = True
        elif boardt[1][1] == boardt[0][2] == boardt[2][0] == 'x':
                flag = True
        if boardt[1][1] == boardt[0][0] == boardt[2][2] == 'o':
                flag = True
        elif boardt[1][1] == boardt[0][2] == boardt[2][0] == 'o':
                flag = True
    return flag
########################################################################################

def winner(boardw):
    win = None
    for row in range(3):
        col = 0
        if boardw[row][col] == boardw[row][col + 1] == boardw[row][col + 2] == 'x':
                win = 'x'
        if boardw[row][col] == boardw[row][col + 1] == boardw[row][col + 2] == 'o':
                win = 'o'
    if win != 'x' or win != 'o':
        for col in range(3):
            row = 0
            if boardw[row][col] == boardw[row + 1][col] == boardw[row + 2][col] == 'x':
                    win = 'x'
            if boardw[row][col] == boardw[row + 1][col] == boardw[row + 2][col] == 'o':
                    win = 'o'
    if win != 'x' or win != 'o':
        if boardw[1][1] == boardw[0][0] == boardw[2][2] == 'x':
                win = 'x'
        elif boardw[1][1] == boardw[0][2] == boardw[2][0] == 'x':
                win = 'x'
        if boardw[1][1] == boardw[0][0] == boardw[2][2] == 'o':
                win = 'o'
        elif boardw[1][1] == boardw[0][2] == boardw[2][0] == 'o':
                win = 'o'
    return win
#########################################################################################

play = input('Do you want to play Tic Tac Toe? (Y/N) ')
if play.lower() == 'n':
    time.sleep(0.5)
    print('Bye, see you soon')

elif play.lower() == 'y':
    time.sleep(0.5)
    play = input('Do you want to play against a Computer or a Player? ')
    
    if play.lower() == 'player':
        lineupnclear(2)
        print('Player 1 is "X"\nPlayer 2 is "O"')
        while not terminal(board):
            printstate()
            plr = plrselect(board)
            move = takeinput()
            board = results(board, move, plr)
            lineupnclear(6)

        if terminal(board):
            if utility(board) == 1:
                printstate()
                print('X Player Wins the game')
            elif utility(board) == -1:
                printstate()
                print('O Player Wins the game')
            elif utility(board) == 0:
                printstate()
                print("It's a DRAW")
    
    
    elif play.lower() == 'computer':
        time.sleep(0.5)
        play = input('Do you want to play as "X" or "O" ')
        lineupnclear(3)
        if play.lower() == 'x':
            human = 'x'
            ai = 'o'
            print('You are "X" Player\nComputer is "O" Player')
            while not terminal(board):
                printstate()
                plr = plrselect(board)
                if ai == plr:
                    time.sleep(1)
                    move = minimax(board, ai)['position']
                    board = results(board, move, plr)
                    print('------------')
                else:
                    move = takeinput()
                    board = results(board, move, plr)
                lineupnclear(6)

            if terminal(board):
                if utility(board) == 1:
                    printstate()
                    print('You Win the game')
                elif utility(board) == -1:
                    printstate()
                    print('Computer Wins the game')
                elif utility(board) == 0:
                    printstate()
                    print("It's a DRAW")
                      
        elif play.lower() == 'o':
            human = 'o'
            ai = 'x'
            print('You are "O" Player\nComputer is "X" Player')
            while not terminal(board):
                printstate()
                plr = plrselect(board)
                if ai == plr:
                    time.sleep(1)
                    move = minimax(board, ai)['position']
                    board = results(board, move, plr)
                    print('------------')
                else:
                    move = takeinput()
                    board = results(board, move, plr)
                lineupnclear(6)
                if terminal(board):
                    if utility(board) == 1:
                        printstate()
                        print('Computer Wins the game')
                    elif utility(board) == -1:
                        printstate()
                        print('You Win the game')
                    elif utility(board) == 0:
                        printstate()
                        print("It's a DRAW")
        else:
             print('Invalid Choice')
    else:
         print('Invalid Choice')
else:
    print('Invalid Choice')
