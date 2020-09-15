from user_input_functions import input_and_validation_from_options
from rules_logic import rules_logic_pre_dealer, rules_logic_post_dealer
from components import Player, Dealer, Deck, Card


# Game settings
number_of_decks = 6
blackjack_multiplier = 1.5
game_rounds = 1000


def main(game_deck, dealer, player): 
    for i in range(1, game_rounds + 1):
        print('----- Round Commencing -----'.format(i))
        player.hit(game_deck)
        dealer.hit(game_deck)
        player.hit(game_deck)
        print('Initial deal details:\n{}\n{}'.format(dealer,  player))
        print('Player turn commencing:')
        player.turn(game_deck)
        dealer_turn_check = rules_logic_pre_dealer(player, dealer, blackjack_multiplier)
        if dealer_turn_check:
            print('Dealer turn commencing:')
            dealer.turn(game_deck)
            rules_logic_post_dealer(player, dealer)
        dealer.reset()
        player.reset()
        game_deck.reset()
        print('----- Round Finished -----'.format(i))


if __name__ == '__main__':  
    # Initialize game deck, dealer and player
    game_deck = Deck(number_of_decks)
    dealer = Dealer()
    player = Player() 
    main(game_deck, dealer, player)














            


