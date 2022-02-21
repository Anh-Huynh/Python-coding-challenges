import os

clear = lambda:os.system('clear')
player = ''
ready = ''

def start_game():
    global player
    global ready
    player = input('Player 1: Do you want to be X or O? ')
    while player.lower() not in ['x', 'o']:
        player = input('Player 1: Do you want to be X or O? ')
        clear()
    print(f'Player 1 ({player}) will go first.')
    
    ready = input('Are you ready to play? Enter Yes or No. ')
    while ready.lower() not in ['yes', 'no', 'y', 'n']:
        ready = input('Are you ready to play? Enter Yes or No. ')
        clear()
    is_ready = ready.lower() in ['yes', 'y']

    if is_ready: 
        play()   
        replay()
    else: 
        replay()

def replay():
    play_again = input('Do you want to play again? Enter Yes or No: ')
    while play_again.lower() not in ['yes', 'no', 'y', 'n']:
        play_again = input('Do you want to play again? Enter Yes or No: ')
        clear()
    is_play_again = play_again.lower() in ['yes', 'y']

    if is_play_again:
        start_game()
    else:
        return

def print_board(position=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']):
    print('   |   |   \n {0} | {1} | {2}  \n   |   |   \n____________\n   |   |   \n {3} | {4} | {5}  \n   |   |   \n____________\n   |   |   \n {6} | {7} | {8}  \n   |   |   \n'.format(*position))

def check_winner(player_set, current_player): 
    global player
    is_winner = False
    # create a dictionary of all possible win patterns in unique sets winsets = {{}, {}, {}}
        # ask Phil why there is TypeError: unhashable type: 'set' if we put winner_pattern in a set??
    winner_patterns = [{0,1,2}, {3,4,5}, {6,7,8}, {0,4,8}, {2,4,6}, {0,3,6}, {1,4,7}, {2,5,8}]
    #loop through each items in the set to find out if any of the item is a subset of player_set
    for winner_pattern in winner_patterns:
        if winner_pattern.issubset(player_set):
            print(f'Congratulations! You ({current_player}) have won the game!')
            is_winner = True
            player = current_player
            break
    return is_winner

def play():
    is_winner = False
    # get the initial player and their choice (X or O)
    global player
    playturn = player.lower()

    # keep track of how many turns has been played and which position has been played. There are total of 9 unique position 
    played_index = set()
    x_played_index = set()
    o_played_index = set()

    required_input = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    # initial display_board
    display_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print_board(display_board)

    #  keep playing when the played position is within 9
    while len(played_index) <= 8 and not is_winner: 
        allowed_input = required_input.difference(played_index)
        if playturn == 'x':
            # get the initial play from user
            x_turn = input('X turn: ')

            # re-promt player for input if their initial input is not within 1-9 or the input has already been played
            while x_turn not in allowed_input:
                x_turn = input('Please enter again! X turn: ')
            
            # update display board and played indexes with the player input
            display_board[int(x_turn)-1] = 'X'
            played_index.add(x_turn)
            x_played_index.add(int(x_turn)-1)

            # update playturn, next turn is O
            playturn = 'o'
            print_board(display_board)
            if len(x_played_index) >= 3:
                is_winner = check_winner(x_played_index, 'X')
    
        elif playturn == 'o':
            y_turn = input('O turn: ')
            while y_turn not in allowed_input:
                y_turn = input('Please enter again! 0 turn: ')
            display_board[int(y_turn)-1] = 'O'
            played_index.add(y_turn)
            o_played_index.add(int(y_turn)-1)
            playturn = 'x'
            print_board(display_board)
            if len(o_played_index) >= 3:
                is_winner = check_winner(o_played_index, 'O')
    if not is_winner:
        print("it's a tight!")
    return
    
start_game()