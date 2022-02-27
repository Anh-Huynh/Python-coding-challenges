from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# single card class that has info about suites, ranks and values of the individual card. We can print it to see the details
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return (f'{self.rank} of {self.suit}')

mycard = Card('Hearts', 'Two')


# deck card class that contains 52 unique sing card. We can perform deal_one() and shuffle() the deck. 
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def deal_one(self):
        if (len(self.all_cards) == 0):
            print('deck is empty')
            return
        else:
            return self.all_cards.pop()

    def shuffle(self):
        shuffle(self.all_cards)

    def __len__(self):
        return len(self.all_cards)

# player class that contains list of cards the player has. It starts with an empty list. The list grows or sinks as player add_cards() or remove_card(). We can view how many cards the player has by calling len()

class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def draw_card(self): 
        return self.all_cards.pop(0)
    def __str__(self):
        return (f'Player {self.name} has {len(self.all_cards)} cards.')


# Game logic

def play_war_game():
    # 1/ Instantiate a deck, shuffle it 
    new_deck = Deck()
    new_deck.shuffle()

    # 2/ Instantiate 2 players
    player_one = Player('Player 1')
    player_two = Player('Player 2')

    # 3/ Split the deck in half and add them onto each player 
    for i in range(int(len(new_deck)/2)):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    # 4/ Game on
    game_on = True
    round = 0
    
    while game_on:
        round += 1
        print(f'Round {round}')

        # check if either of the player run out of cards
        if (len(player_one.all_cards) == 0):
            print("Player One out of cards! Game Over")
            print("Player Two Wins!")
            game_on = False
            break
        if (len(player_two.all_cards) == 0 ):
            print("Player Two out of cards! Game Over")
            print("Player One Wins!")
            game_on = False
            break

        # Otherwise, each player put one card in the table on each new round

        player_one_draw_cards = [player_one.draw_card()]
        player_two_draw_cards = [player_two.draw_card()]

        at_war = True

        while at_war:
            player_one_value = 0
            player_two_value = 0


            # calculate value of each player cards on the table
            for i in range(0, int(len(player_one_draw_cards)) ): 
                player_one_value += player_one_draw_cards[i].value
                player_two_value += player_two_draw_cards[i].value


            # determine who will get the cards on the table by comparing their values
            if (player_one_value > player_two_value): 
                player_one.add_cards(player_one_draw_cards)
                player_one.add_cards(player_two_draw_cards)
                at_war = False

            elif (player_one_value < player_two_value): 
                player_two.add_cards(player_one_draw_cards)
                player_two.add_cards(player_two_draw_cards)
                at_war = False

            # if their values are equal, the war begins
            else:
                print('At War!!')

                if len(player_one.all_cards) < 5:
                        print("Player One unable to play war! Game Over at War")
                        print("Player Two Wins! Player One Loses!")
                        game_on = False
                        break
                if len(player_two.all_cards) < 5:
                        print("Player Two unable to play war! Game Over at War")
                        print("Player One Wins! Player Two Loses!")
                        game_on = False
                        break
                #draw additional 5 cards and append them to the existing cards on the table
                for i in range(5):
                    player_one_draw_cards.append(player_one.draw_card())
                    player_two_draw_cards.append(player_two.draw_card())

                #the at_war loop continue until it resolves the war. Then it continues the outer game_on loop with a new round. 
                


play_war_game()



