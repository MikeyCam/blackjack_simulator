import random

suits = ("S","H","C","D")
number_of_decks = 3

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        if self.rank == 1:
            true_rank = "A"
        elif self.rank == 11:
            true_rank = "J"
        elif self.rank == 12:
            true_rank = "Q"
        elif self.rank == 13:
            true_rank = "K"
        else:
            true_rank = str(self.rank)
        return "Card: {}{}".format(true_rank, self.suit)

    def get_card_score(self):
        if self.rank == 1:
            score = [1,11]
        elif self.rank >= 11 and self.rank <= 13:
            score = 10
        else:
            score = self.rank 
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
        image_loc = "card_images\{}.png".format(self)
        return image_loc



class Deck:
    def __init__(self, int:number_of_decks):
        self.number_of_decks = number_of_decks
        self.cards = []
        self.create(self.number_of_decks)

    def __repr__(self):
        return "GameDeck: {} cards".format(len(self.cards))
    
    def create(self, number_of_decks):
        decks = [Card(rank, suit) for suit in suits for rank in range(1, 14) for deck in range(number_of_decks)]
        decks = random.sample(decks, len(decks))
        self.cards.extend(decks)

    def draw(self):
        drawn_card = self.cards[0]   
        self.cards.remove(self.cards[0])
        return drawn_card


class Player:
    def __init__(self, buy_in):
        self.cards = []
        self.buy_in = buy_in

    def hit(self):
        pass

    def split(self):
        pass

    def hold(self):
        pass

class Dealer(Player):
    pass





def main():
    #game_start = input("Do you want to play BlackJack? (Y/N) : ").lower()
    #if game_start == 'y':
    print("Welcome to Python Casino, let's deal!")
    game = Deck(number_of_decks)

if __name__ == "__main__":
    main()














            


