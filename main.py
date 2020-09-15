from user_input_function import input_and_validation_from_options
from rules_logic import rules_logic_pre_dealer, rules_logic_post_dealer
from components import Player, Dealer, Deck, Card
from round import round

# Game settings
number_of_decks = 6
blackjack_multiplier = 1.5
game_rounds = 1
# Set user_input to true if you want to input your own choice, false if you want outcomes to be random.
user_input = False

# Initialize player, dealer and deck
game_deck = Deck(number_of_decks)
dealer = Dealer()
player = Player(user_input)


def main(game_deck, dealer, player):
    for i in range(1, game_rounds + 1):
        print('----- ROUND {} -----'.format(i))
        round(game_deck, dealer, player, blackjack_multiplier)
        


if __name__ == '__main__':
    main(game_deck, dealer, player)
