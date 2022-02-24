
import os
import random
from re import X

clear_output = lambda:os.system('clear')

#print out a board
def display_board(board):
    # clear_output()
    print('   |   |   \n {1} | {2} | {3}  \n   |   |   \n____________\n   |   |   \n {4} | {5} | {6}  \n   |   |   \n____________\n   |   |   \n {7} | {8} | {9}  \n   |   |   \n'.format(*board))

# get player input and return a tuple of markers
def player_input():
    marker = ''
    while not (marker=='X' or marker=='O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker=='X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# assign a marker to a desired position in the board
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    # filter out all positions that has mark
    player_positions = set()
    for (index, value) in enumerate(board):
        if value == mark:
            player_positions.add(index)
    
    # create a set of all possible winning tuples
    win_positions = [{1,2,3}, {4,5,6}, {7,8,9}, {1,5,9}, {3,5,7}, {1,4,7}, {2,5,8}, {3,6,9}]
    
    # iterate on each tuple, if it is a subset of mark list
    for position in win_positions:
        if position.issubset(player_positions):
            return True
    return False

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]

def player_choice(board):
    player_next_position = 0
    
    while player_next_position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, player_next_position):
        player_next_position = int(input ('Choose your next position: (1-9) '))
    
    return player_next_position

def replay():
    replay = ''
    while replay not in ['yes', 'no', 'y', 'n']:
        replay = input('Do you want to play again? Enter Yes or No: ')
    return replay.lower().startswith('y')

def play_ready():
    ready = ''
    while ready not in ['yes', 'no', 'y', 'n']:
        ready = input('Are you ready to play? Enter Yes or No: ')
    return ready.lower().startswith('y')


def play_tic_tac_toe():
    
    print('Welcome to Tic Tac Toe!')

    # outer loop always run unless being break out
    while True:
        # set up the game
        board = [' ']*10
        (player1_marker, player2_marker) = player_input()
        turn = choose_first()
        print(f'{turn} will go first.')
        ready = play_ready()

        if ready:
            game_on = True
        else:
            game_on = False
        
        while game_on:
            #Player 1 Turn
            if turn == 'Player 1': 
                display_board(board)
                player1_choice = player_choice(board)
                place_marker(board,player1_marker, player1_choice)

                if win_check(board, player1_marker):
                    display_board(board)
                    print('Congratulations! You have won the game!')
                    game_on = False
                elif full_board_check(board):
                    display_board(board)
                    print('It s a draw')
                    break
                else:
                    turn = 'Player 2'

            # Player2's turn.
            if turn == 'Player 2': 
                display_board(board)
                player2_choice = player_choice(board)
                place_marker(board,player2_marker, player2_choice)
                
                if win_check(board, player2_marker):
                    display_board(board)
                    print('Player2 have won the game!')
                    game_on = False
                elif full_board_check(board):
                    display_board(board)
                    print('It s a draw')
                    break
                else:
                    turn = 'Player 1'

        if not replay():
            break

play_tic_tac_toe()