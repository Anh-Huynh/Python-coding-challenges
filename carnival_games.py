# There will be 3 positions in the list, one of which is an 'O', a function will shuffle the list, another will take a player's guess, and finally another will check to see if it is correct. This is based on the classic carnival game of guessing which cup a red ball is under.

import random

def shuffle_list (list):
    random.shuffle(list)
    return list

def player_guess():
    guess = ''
    while guess not in ['1','2','0']:
        guess = input("Pick a number: 0, 1, or 2:  ")
    return int(guess)

def check_guess(list, guess):
    if list[guess] == '0':
        print(f'Your answer is right! \n {list}')
    else:
        print('Wrong! Better luck next time {}'.format(list))

def carnival_games(list):
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2:  ")
        continue
    random.shuffle(list)
    if list[int(guess)] == '0':
        print(f'Your answer is right! \n {list}')
    else:
        print('Wrong! Better luck next time {}'.format(list))

#play game
mylist = [' ','O',' ']
carnival_games(mylist)
