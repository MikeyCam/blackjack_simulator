import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.get_card_scores()
    
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

    def get_card_scores(self):
        if self.rank == 1:
            card_scores = [1,11]
        elif self.rank >= 11 and self.rank <= 13:
            card_scores = [10,10]
        else:
            card_scores = [self.rank, self.rank]
        return card_scores




class Deck:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.cards = []
        self.create(self.number_of_decks)

    def __repr__(self):
        return 'Game deck has {} cards remaining'.format(len(self.cards))
    
    def create(self, number_of_decks):
        decks = [Card(rank, suit) for suit in suits for rank in range(1, 14) for deck in range(number_of_decks)]
        decks = random.sample(decks, len(decks))
        self.cards.extend(decks)

    def draw(self):
        drawn_card = self.cards[0] 
        self.cards.remove(self.cards[0])
        return drawn_card


class Dealer:
    def __init__(self):
        self.cards = []
        self.hand_scores = [0,0]
        self.best_outcome = 'Awaiting deal'

    def __repr__(self):
        return 'Dealer Hand: {}, Scores: {}, Best Outcome: {}'.format(self.cards, list(set(self.hand_scores)), self.best_outcome)

    def hit(self, game_deck):
        draw_card = game_deck.draw()
        self.cards.append(draw_card)
        card_scores = draw_card.get_card_scores()
        self.hand_scores = [a + b for a, b in zip(self.hand_scores, card_scores)]
        if len(self.cards) <= 1 :
            self.best_outcome  = 'Awaiting Deal'
        elif 21 in self.hand_scores and len(self.cards) == 2:
            self.best_outcome  = 'BlackJack'
        elif all(self.hand_scores) > 21:
            self.best_outcome = 'Bust'
        else:
            self.best_outcome  = max([i for i in self.hand_scores if i <=21])


    def reset(self):
        self.cards.clear()
        self.hand_scores = [0,0]
        self.best_outcome = 'Awaiting deal'
    



class Player(Dealer):
    def __init__(self):
        self.cards = []
        self.hand_scores = [0,0]
        self.best_outcome = 'Awaiting deal'
        self.possible_actions = []

    def __repr__(self):
        return 'Player Hand: {}, Scores: {}, Best Outcome: {}'.format(self.cards, list(set(self.hand_scores)), self.best_outcome)

    def turn(self):
        pass


    
    
def blackjack_check(dealer, player):
    pass




# Game settings
suits = ('Spades','Hearts','Clubs','Diamonds')
number_of_decks = 3
player_options = ['Hit(H)', 'Double down(D)', 'Stand(S)']
buy_in = 1000
betting_increment = 50
blackjack_multiplier = 1.5
game_rounds = 10




def main(game_deck, dealer, player): 
    print("Welcome to the Python Casino (Blackjack only)")
    for i in range(1, game_rounds + 1):
        print('----- Round {} -----'.format(i))
        player.hit(game_deck)
        dealer.hit(game_deck)
        player.hit(game_deck)
        print('Opening Details:\n{}\n{}\n{}'.format(dealer,  player,  game_deck))
        blackjack_check(dealer, player)
        print('Player turn:')
        player.turn()
        dealer.hit(game_deck)
        print('Dealer Turn Details:\n{}\n{}\n{}'.format(dealer,  player,  game_deck))
        #turn_outcome()
        dealer.reset()
        player.reset()


if __name__ == '__main__':  
    # Initialize game deck, dealer and player
    game_deck = Deck(number_of_decks)
    dealer = Dealer()
    player = Player() 
    main(game_deck, dealer, player)














            


