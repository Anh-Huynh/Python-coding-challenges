'''
Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet_amount
Make sure that the Player's bet_amount does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again
'''
from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':(10, 1)}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f'{self.suit} of {self.rank}'

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    def shuffle(self):
        shuffle(self.all_cards)
    def deal(self):
        return self.all_cards.pop(0)
    def __len__(self):
        return len(self.all_cards)
    def __str__(self):
        return f'Deck has {len(self.all_cards)} cards left'
class Hand:
    def __init__(self):
        self.all_cards = []
        self.values = 0
    def add_card(self, card):
        self.all_cards.append(card)
        # Aces have a rank of either 11 or 1 as needed to reach 21 without busting
        if not card.rank == 'Ace':
            self.values += int(card.value)
        else:
            if self.values + 11 <= 21:
                self.values += 11
                print('ace value 11 has been added')
            else: 
                self.values += 1
                print('ace value 1 has been added')
        if self.values > 21:
            return 'Burst'
    def __str__(self):
        return f'I have {len(self.all_cards)} cards with total value of {self.values}'

class Chips:
    def __init__(self, total):
        self.total = total
    def win_bet(self, bet_amount):
        self.total += bet_amount
    def loose_bet(self, bet_amount):
        self.total -= bet_amount
    def bet_not_valid(self, bet_amount):
        return bet_amount > self.total
    def __str__(self):
        return f'You have total {self.total} chips'

def show_some_cards(playerhand, dealerhand):
    print("Dealer's Hand: ")
    print("<card hidden>")
    for card in dealerhand.all_cards[1:]:
        print(card)
    print("\nPlayer's Hand: ")
    for card in playerhand.all_cards:
        print (card)

def show_all_cards(playerhand, dealerhand):
    print("Dealer's Hand: ")
    for card in dealerhand.all_cards:
        print(card)
    print(f"Dealer's Hand = {dealerhand.values}")
    print("\nPlayer's Hand: ")
    for card in playerhand.all_cards:
        print (card)
    print(f"Player's Hand = {playerhand.values}")

class GameError(Exception):
    pass
class NotValidBet(GameError):
    pass
def take_bet(player_chips):
    while True:
        try:
            bet_amount = int(input('How many chips would you like to bet? '))
            if player_chips.bet_not_valid(bet_amount):
                raise NotValidBet
            break
        except ValueError:
            print('Please enter an integer')
            continue
        except NotValidBet:
            print('Your bet exceeds your available chips')
            continue
    return bet_amount

class HitError(GameError):
    pass
def hit_or_stand():
    while True:
        try:
            hit_or_stand = input(f"Would you like to Hit or Stand? Enter 'h' or 's' ")
            if hit_or_stand not in['h','s']: 
                raise HitError
            break
        except HitError:
            print("Enter 'h' or 's' only!")
    return hit_or_stand

def play_blackjack():
    #assign an initial chips to player and create a new deck
    player_chips = Chips(100)
    deck = Deck()

    game_on = True
    while game_on:
        print('Welcome to BlackJack! Get as close to 21 as you can without going over! Dealer hits until she reaches 17. Aces count as 1 or 11.')
        #get player's bet_amount
        player_bet = take_bet(player_chips)

        # shuffle the deck and deal 2 cards for Player and Dealer
        deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        for i in range(2):
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

        # show both dealer hand and player hand 
        show_some_cards(player_hand, dealer_hand)

        # start with player round first. it will determine if dealer ever need to start their round. Reset bursting variables incase player plays multiple hands.
        player_playing = True
        dealer_playing = False
        is_player_burst = False
        is_dealer_burst = False

        # start player's loop  
        while player_playing:
            # Ask the Player if they wish to Hit
            player_hit_or_stand = hit_or_stand()
            # If player stands, break out of the loop and play the Dealer's hand
            if player_hit_or_stand == 's':
                print('Player stands. Dealer is playing')
                dealer_playing = True
                break
            # Otherwise, deal one card to player and determine if player can continue hitting or burst
            else:
                is_player_burst = player_hand.add_card(deck.deal())
                if is_player_burst: 
                    break
                else:
                    show_some_cards(player_hand, dealer_hand)
                    continue 

        # start dealer loop if condition allows
        while dealer_playing and dealer_hand.values < 17:
            # keep hitting until dealer bust or their value >= 17
            is_dealer_burst = dealer_hand.add_card(deck.deal())
            if is_dealer_burst or dealer_hand.values >= 17:
                break

        # anounce winner in different cases      
        if is_player_burst:
            player_chips.loose_bet(player_bet)
            print('Player bursts!Dealer wins!')
        elif is_dealer_burst:
            player_chips.win_bet(player_bet*2)
            print('Dealer bursts!Plaer wins!')
        else:
            show_all_cards(player_hand, dealer_hand)
            if player_hand.values > dealer_hand.values:
                player_chips.win_bet(player_bet)
                print('Player wins!')
            elif player_hand.values < dealer_hand.values:
                player_chips.loose_bet(player_bet)
                print('Dealer wins!')
            else:
                print("It's a tight!")
        
        print(f'Currently you have {player_chips.total} chips')

        # if player wish to play another hand, continue the outer loop. otherwise, break the outer loop to end the game by setting game_on to False
        while True:
            play_again = input("Would you like to play another hand? Enter 'y' or 'n' ")
            if play_again == 'y':
                break
            elif play_again =='n':
                print('Thank you for playing!')
                game_on = False
                break

play_blackjack()
