from time import sleep
from math import inf
from copy import deepcopy
from random import choice
clear, up, continue_game, x, o = '\x1b[2K', '\033[1A', 'y', 'x', 'o'
board = [[' ']*3 for _ in range(3)]
###############################################################################################################################################
def moveupnclearline(num):
    for _ in range(num): print(up, end = clear)
###############################################################################################################################################
def print_board_state(boardps):
    for row in boardps: print(' ' + ' | '.join(row), '-----------', sep = '\n')
    moveupnclearline(1)
###############################################################################################################################################
def retakeinput(boardrti):
    moveupnclearline(6)
    print("Choose another block / InValid Syntax")
    sleep(2)
    moveupnclearline(1)
    print_board_state(boardrti)
    return takeinput(boardrti)
###############################################################################################################################################
def takeinput(boardti):   
    position = input('Number Grid (7,8,9...): ')
    if position.isdigit() and 0 < int(position) < 10 :
        allpositions = ['20','21','2','10','1','12','0','01','02']
        position = allpositions[int(position)- 1]
        if boardti[int(position[:1])][int(position[-1:])] != ' ': return retakeinput(boardti)
        return position
    else: return retakeinput(boardti)
###############################################################################################################################################
def playerselect(boardp):
    empty, xmoves, omoves = 0, 0, 0
    for i in range(3):
        for j in range(3):
            empty = empty + 1 if boardp[i][j] == ' ' else empty
            xmoves = xmoves + 1 if boardp[i][j] == x else xmoves
            omoves = omoves + 1 if boardp[i][j] == o else omoves
    return x if empty == 9 or xmoves == omoves else o
###############################################################################################################################################
def actions(boarda):return [f'{i}{j}' for i in range(3) for j in range(3) if boarda[i][j] == ' ']
###############################################################################################################################################
def apply_move(boardr, actionr, playerr):
    duplicate = deepcopy(boardr)
    duplicate[int(actionr[:1])][int(actionr[-1:])] = playerr
    return duplicate
###############################################################################################################################################
def terminal(boardt):
    for index in range(3):
        if boardt[index][0] == boardt[index][1] == boardt[index][2] != ' ': return boardt[index][0]
        if boardt[0][index] == boardt[1][index] == boardt[2][index] != ' ': return boardt[0][index]
    if boardt[1][1] == boardt[0][0] == boardt[2][2] != ' ': return boardt[1][1]
    if boardt[1][1] == boardt[0][2] == boardt[2][0] != ' ': return boardt[1][1]
    empty = sum([1 for row in range(3) for col in range(3) if boardt[row][col] == ' '])
    return '-' if empty == 0 else None
###############################################################################################################################################
def announce_results(boardar, x_player, o_player):
    wnr = terminal(boardar)
    print_board_state(boardar)
    print(f'{x_player} Won!!!' if wnr == x else f'{o_player} Won!!!' if wnr == o else "It's a Draw :p" if wnr == '-' else '', )
###############################################################################################################################################
def prompt_continue(boardc):
    if terminal(boardc):return input('Continue Playing? (Y)es or (N)o:  ')
###############################################################################################################################################
def minimax(boardm, mainplayer, alpha, beta, depth):
    final_state = terminal(boardm)
    if mainplayer == x: otherplayer, best = o, {'position':None, 'score':-inf}
    else: otherplayer, best = x, {'position':None, 'score':inf}
    if final_state == x: best['score'] = (1/depth) + 1
    elif final_state == o: best['score'] = (-1/depth) - 1
    elif final_state == '-': best['score'] = 0
    else:
        for action in actions(boardm):
            if depth < 9:
                maybebest = minimax(apply_move(boardm, action, mainplayer), otherplayer, alpha, beta, depth + 1)
                maybebest['position'] = action
                if mainplayer == x:
                    best = maybebest if maybebest['score'] > best['score'] else best
                    alpha = max(alpha, best['score'])
                else:
                    best = maybebest if maybebest['score'] < best['score'] else best
                    beta = min(beta, best['score'])
                if beta <= alpha: break
            else: break
    return best
###############################################################################################################################################
def game(boardg, person1, person2):
    player1, player2, playermove1, playermove2 = person1[:-1], person2[:-1], person1[-1:], person2[-1:]
    print(f"It's {player1}({playermove1.upper()}) vs {player2}({playermove2.upper()}) ;)")
    while not terminal(boardg):
        print_board_state(boardg)
        currentplayer, currentmove = (player1, playermove1) if playermove1 == playerselect(boardg) else (player2, playermove2)
        if currentplayer == 'You' or currentplayer == 'Other Player': boardg = apply_move(boardg, takeinput(boardg), currentmove)
        elif currentplayer == 'Computer':
            boardg = apply_move(boardg, choice(actions(boardg)), currentmove)
            print('Thinking...')
            sleep(0.5)
        else:
            boardg = apply_move(boardg, minimax(boardg, currentmove, -inf, inf, 0)['position'], currentmove)
            print('Thinking...')
            sleep(0.5)
        moveupnclearline(6)
    announce_results(boardg, player1 if playermove1 == x else player2,  player1 if playermove1 == o else player2)
    return prompt_continue(boardg)
###############################################################################################################################################
moveupnclearline(1)
print('Welcome to Tic Tac Toe :)')
while continue_game == 'y':
    choose = input('Do YOU want to play? (Y)es or (N)o:  ').lower()
    if choose == 'n':
        moveupnclearline(1)
        continue_game = game(board, f'Computer{x}', f'AI{o}')
    elif choose == 'y':
        choose = input('Select Opponent; (C)omputer or (P)layer:  ').lower()
        if choose == 'p':
            moveupnclearline(3)
            continue_game = game(board,f'You{x}', f'Other Player{o}')
        elif choose == 'c':
            move = input(f'Do you want to play as ({x.upper()}) or ({o.upper()}):  ').lower()
            if move == x or move == o:
                choose = input('Select Difficulty; (E)asy or (G)enius:  ').lower()
                if choose == 'g':
                    moveupnclearline(5)
                    continue_game = game(board, f'You{x}' if move == x else f'AI{x}', f'You{o}' if move == o else f'AI{o}')
                elif choose == 'e':
                    moveupnclearline(5)
                    continue_game = game(board, f'You{x}' if move == x else f'Computer{x}', f'You{o}' if move == o else f'Computer{o}')
                else:
                    print('Invalid Choice')    
            else:
                print('Invalid Choice')
        else:
            print('Invalid Choice')
    else:
        print('Invalid Choice')