import random

suits = ('S','H','C','D')
number_of_decks = 3

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        if self.rank == 1:
            true_rank = 'A'
        elif self.rank == 11:
            true_rank = 'J'
        elif self.rank == 12:
            true_rank = 'Q'
        elif self.rank == 13:
            true_rank = 'K'
        else:
            true_rank = str(self.rank)
        return 'Card: {}{}'.format(true_rank, self.suit)

    def get_card_score(self):
        if self.rank == 1:
            score = {'Score 1': 1, 'Score 2': 11}
        elif self.rank >= 11 and self.rank <= 13:
            score = {'Score 1': 10, 'Score 2': 10}
        else:
            score = {'Score 1': self.rank , 'Score 2': self.rank }
        return score

    def get_card_counting_value(self):
        if self.rank >= 2 and self.rank <= 6:
            card_counting_value = 1
        elif self.rank >= 7 and self.rank <= 9:
            card_counting_value = 0
        else:
            card_counting_value = -1
        return card_counting_value

    def get_image(self):
        image_loc = 'card_images\{}.png'.format(self)
        return image_loc



class Deck:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.cards = []
        self.drawn_cards = []
        self.create(self.number_of_decks)

    def __repr__(self):
        return 'GameDeck: {} cards'.format(len(self.cards))
    
    def create(self, number_of_decks):
        decks = [Card(rank, suit) for suit in suits for rank in range(1, 14) for deck in range(number_of_decks)]
        decks = random.sample(decks, len(decks))
        self.cards.extend(decks)

    def draw(self):
        drawn_card = self.cards[0]   
        self.cards.remove(self.cards[0])
        self.drawn_cards.append(drawn_card)
        return drawn_card


class Dealer:
    def __init__(self):
        self.cards = []
        self.score()
        self.outcome()

    def __repr__(self):
        return 'Hand: {}'.format(self.cards)

    def score(self):
        final_score = {'Score 1': 0 , 'Score 2': 0}
        for card in self.cards:
            score = card.get_card_score()
            final_score = {k: final_score.get(k) + score.get(k) for k in set(final_score)}
        return final_score

    def outcome(self):
        final_outcome = {'Score 1': 'NA' , 'Score 2': 'NA'}
        for i in self.score():
            if len(self.cards) == 0 :
                final_outcome[i] = 'Awaiting Deal'
            elif self.score()[i] == 21 and len(self.cards) == 2:
                final_outcome[i] = 'BlackJack'
            elif self.score()[i] > 21:
                final_outcome[i] = 'Bust'
            else:
                final_outcome[i] = self.score()[i]
        return final_outcome   

    def hit(self, game_deck):
        draw_card = game_deck.draw()
        self.cards.append(draw_card)



class Player(Dealer):
    def __init__(self, cash_balance):
        self.cards = []
        self.cash_balance = cash_balance




        
def initial_deal(game_deck, dealer, player):
    draw_card = game_deck.draw()
    player.cards.append(draw_card)
    draw_card = game_deck.draw()
    dealer.cards.append(draw_card)
    draw_card = game_deck.draw()
    player.cards.append(draw_card)
    draw_card = game_deck.draw()
    dealer.cards.append(draw_card)


def turn(game_deck, dealer, player):
    pass




def main():
    game_deck = Deck(5)
    dealer = Dealer()
    player = Player(1000)
    initial_deal(game_deck, dealer, player)
    print(dealer)
    print(dealer.cards)
    print(dealer.score())
    print(len(dealer.cards))
    print(dealer.outcome())
    print(player)
    print(player.score())
    print(player.outcome())
    print(dealer.hit(game_deck))
    print(dealer)
    print(dealer.score())
    print(dealer.outcome())
    print(player.hit(game_deck))
    print(player)
    print(player.score())
    print(player.outcome())
 
    

if __name__ == '__main__':
    main()














            


