from user_input_function import input_and_validation_from_options
from rules_logic import rules_logic_pre_dealer, rules_logic_post_dealer
from components import Player, Dealer, Deck, Card


def round(game_deck, dealer, player, blackjack_multiplier):
    player.hit(game_deck)
    dealer.hit(game_deck)
    player.hit(game_deck)
    print('Initial deal details:\n{}\n{}'.format(dealer,  player))
    print('Player turn commencing:')
    player.turn(game_deck)
    dealer_turn_check = rules_logic_pre_dealer(
        player, dealer, blackjack_multiplier)
    if dealer_turn_check:
        print('Dealer turn commencing:')
        dealer.turn(game_deck)
        rules_logic_post_dealer(player, dealer)
    dealer.reset()
    player.reset()
    game_deck.reset()
