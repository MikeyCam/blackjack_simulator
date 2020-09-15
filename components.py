import random
from user_input_function import input_and_validation_from_options

suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if self.rank == 1:
            self.card_scores = [1, 11]
        elif self.rank >= 11 and self.rank <= 13:
            self.card_scores = [10, 10]
        else:
            self.card_scores = [self.rank, self.rank]

    def __repr__(self):
        if self.rank == 1:
            true_rank = 'Ace'
        elif self.rank == 11:
            true_rank = 'Jack'
        elif self.rank == 12:
            true_rank = 'Queen'
        elif self.rank == 13:
            true_rank = 'King'
        else:
            true_rank = str(self.rank)
        return '{} of {}'.format(true_rank, self.suit)


class Deck:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.cards = []
        self.create(self.number_of_decks)

    def __repr__(self):
        return 'Game deck has {} cards remaining'.format(len(self.cards))

    def create(self, number_of_decks):
        decks = [Card(rank, suit) for suit in suits for rank in range(1, 14)
                 for deck in range(number_of_decks)]
        decks = random.sample(decks, len(decks))
        self.cards.extend(decks)

    def draw(self):
        drawn_card = self.cards[0]
        self.cards.remove(self.cards[0])
        return drawn_card

    def reset(self):
        self.create(self.number_of_decks)


class Dealer:
    def __init__(self):
        self.cards = []
        self.hand_scores = [0, 0]
        self.best_outcome = 'Awaiting deal'

    def __repr__(self):
        return 'Dealer Hand: {}, Scores: {}, Best Outcome: {}'.format(self.cards, list(set(self.hand_scores)), self.best_outcome)

    def hit(self, game_deck):
        draw_card = game_deck.draw()
        self.cards.append(draw_card)
        card_scores = draw_card.card_scores
        self.hand_scores = [a + b for a,
                            b in zip(self.hand_scores, card_scores)]
        if len(self.cards) <= 1:
            self.best_outcome = 'Awaiting Deal'
        elif 21 in self.hand_scores and len(self.cards) == 2:
            self.best_outcome = 'Blackjack'
        elif self.hand_scores[0] > 21 and self.hand_scores[1] > 21:
            self.best_outcome = 'Bust'
        else:
            self.best_outcome = max([i for i in self.hand_scores if i <= 21])

    def turn(self, game_deck):
        self.hit(game_deck)
        print(self.__repr__())
        if self.best_outcome == 'Blackjack':
            print('Dealer hit Blackjack')
        elif self.best_outcome == 'Bust':
            print('Dealer went Bust')
        elif int(self.best_outcome) < 17:
            print('Dealer has {}, Dealer has to hit'.format(self.best_outcome))
            self.turn(game_deck)
        else:
            print('Dealer is proceeding with {}'.format(self.best_outcome))

    def reset(self):
        self.cards.clear()
        self.hand_scores = [0, 0]
        self.best_outcome = 'Awaiting deal'


class Player(Dealer):
    def __init__(self, user_input):
        self.cards = []
        self.hand_scores = [0, 0]
        self.best_outcome = 'Awaiting deal'
        self.possible_actions = []
        self.double_down = False
        self.ROI = 0
        self.user_input = user_input

    def __repr__(self):
        return 'Player Hand: {}, Scores: {}, Best Outcome: {}'.format(self.cards, list(set(self.hand_scores)), self.best_outcome)

    def turn(self, game_deck):
        print(self.__repr__())
        if self.best_outcome == 'Blackjack':
            print('Player hit Blackjack')
            return
        if self.best_outcome == 'Bust':
            print('Player went Bust')
            return
        if self.double_down == True:
            print('Player is proceeding with {}'.format(self.best_outcome))
            return
        if len(self.cards) == 2:
            self.possible_actions = ['Hit(h)', 'Stand(s)', 'Double Down(d)']
            if self.user_input:
                decision = input_and_validation_from_options(
                    self.possible_actions)
            else:
                decision = random.choice(self.possible_actions)
            if decision == 'Double Down(d)':
                print('Player has doubled down')
                self.double_down = True
                self.hit(game_deck)
                self.turn(game_deck)
            elif decision == 'Hit(h)':
                print('Player has hit')
                self.hit(game_deck)
                self.turn(game_deck)
            elif decision == 'Stand(s)':
                print('Player is standing and proceeding with {}'.format(
                    self.best_outcome))
        elif len(self.cards) > 2:
            self.possible_actions = ['Hit(h)', 'Stand(s)']
            if self.user_input:
                decision = input_and_validation_from_options(
                    self.possible_actions)
            else:
                decision = random.choice(self.possible_actions)
            if decision == 'Hit(h)':
                print('Player has hit')
                self.hit(game_deck)
                self.turn(game_deck)
            elif decision == 'Stand(s)':
                print('Player is standing and proceeding with {}'.format(
                    self.best_outcome))
        else:
            print('Check decision matrix')

    def reset(self):
        self.cards = []
        self.hand_scores = [0, 0]
        self.best_outcome = 'Awaiting deal'
        self.possible_actions = []
        self.double_down = False
        self.ROI = 0
