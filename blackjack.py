'''
Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again
'''

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':(10, 1)}

print(values['Ace'])

# create Card object 
    # properties: suits, ranks, value
    # methods: __str__()

# create Deck object that hold a list of 52 different Cards
    # properties: all_cards

    # methods: shuffle(), deal(), hit(), __len__()

# create Bank object
    # properties: all_chips, all_cards
    # methods: remove_chips(make sure it does not exceed available chips), add_chips()

# create show_cards(role, cards) function
    # check role
        #Show only one of the Dealer's cards, the other remains hidden
        #Show both of the Player's cards
        #  Dealer's Hand:
        #  <card hidden>
        #  Ten of Spades

        # Player's Hand:
        #  Ten of Diamonds
        #  Six of Hearts

# show_dealer_hand

# show_player_hand

# create is_Burst(cards) function
   # return True if the total card value is over 21

# creat is_Exceed(value) ? maybe


# Game logic

# outer loop while 
    # print(Welcome to BlackJack! Get as close to 21 as you can without going over! Dealer hits until she reaches 17. Aces count as 1 or 11.)

    # get player's bet
        # How many chips would you like to bet? 
        # if bet exceeds available chips keep asking

    # deal 2 cards for Player and Dealer

    # show both dealer hand and player hand 

    # while is_burst == False and game_on == True // may not need

# player_playing = True
# dealer_playing = False

# start player's loop  
# Ask the Player if they wish to Hit, and take another card
# If is_stand, break out of the loop and play the Dealer's hand
    # add the card onto Player's hand
    # set dealer_playing = True
    # Print: Player stands. Dealer is playing.
    # break out of the loop
# Otherwise, check total Player's value
    # If the value < 21, start over the loop.
    # If value > 21, set is_player_burst TRUE break out of this loop 

# While dealer_playing = True & Dealer value < 17
    # keep hitting 
    # when value >= 17
        # if value > 21, set is_dealer_burst = TRUE
        # break out of this loop 



# if is_player_burst:
    # announce Dealer wins
    # adjust Player's chips
# elif is_Dealer_burst:
    # announce player wins
    # adjust Player's chips. they get double chips in this case
# else: compare Player value with Dealer value 
    # reveal all the cards and its values
    # announce the winner
    # adjust Player's chips

# announce Player's total chips

# Would you like to play another hand? Enter 'y' or 'n'
    # if yes, start over at the beginning of outer loop
    # if no, break out of the outer loop and end the game


