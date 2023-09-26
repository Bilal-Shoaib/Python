from random import choice
from time import sleep
clear, up, continue_game = '\x1b[2K', '\033[1A', 'y'
classes = {'Automotive':['ferrari','lamborghini','pagani','koenigsegg','bugatti','lexus','porsche','alfa romeo'],
           'Watch':['cartier','rolex','omega','casio','tissot','fossil','diesel','guess','audemars piguet','patek philippe'],
           'Smart Phone':['samsung','google','oneplus','apple','xiaomi','oppo','motorola'],
           'Clothing':['prada','gucci','armani','dior','chanel','nike','adidas','louis vuitton','michael kors']}
###############################################################################################################################################
def moveupnclearline(num):
    for _ in range(num): print(up, end = clear)
###############################################################################################################################################
def print_hangman(foulsp):
    if foulsp > 1: print('You lose\n      |`````|')
    if foulsp > 2: print('    (~_~)   |')
    if foulsp > 3: print('    /| |\   |')
    if foulsp > 4: print('    _/ \_   |\n            |\nTTTTTTTTTTTTTTTTT')
###############################################################################################################################################
def automate():
    automatic_selection = choice(list(classes.keys()))
    print(f'Hint: {automatic_selection} Brand')
    return classes[automatic_selection]
###############################################################################################################################################
def game():
    print('Guess a letter')
    main_array = automate()
    word = choice(main_array)
    answer, guesses, fouls = '_'*len(word), '', 0
    if ' ' in word:
        for count in range(len(word)):
            if ' ' == word[count:count+1]: answer = answer[:count]+answer[count].replace('_',' ')+answer[count+1:]
    while answer != word and fouls < 5:
        print(answer, end = '\r')
        character = input()
        if character in guesses or not ('a'<=character.lower()<='z') : 
            moveupnclearline(1)
            print('You have already guessed this, or it is an unsupported key. Retry')
            sleep(2)
            moveupnclearline(1)
            continue
        guesses += character
        if character in word:    
            for index in range(len(word)):
                if character == word[index:index+1]: answer = answer[:index]+answer[index].replace('_',character)+answer[index+1:]
        else:
            print(up+'Incorrect :(')
            sleep(2)
            fouls += 1
        moveupnclearline(1)
    moveupnclearline(2)
    print(f'YOU WIN!!!!!\nThe correct word was: {word.title()}\nWell Played ;)') if word == answer else print_hangman(fouls)
    return input('Continue Playing? (Y)es:  ')
###############################################################################################################################################
moveupnclearline(1)
print('Welcome to Hangman :)')
print('You can only Blunder 5 times\nGOOD LUCK ;)')
sleep(2)
moveupnclearline(2)
while continue_game == 'y':
    continue_game = game()
    moveupnclearline(1)
