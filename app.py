import streamlit as st
from PIL import Image
from components import GamePlay, Player, Dealer, Deck


# Game settings
number_of_decks = 6
blackjack_multiplier = 1.5


# Initialize player, dealer, deck and game play. Cache these variables
@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def start_game():
    game_deck = Deck(number_of_decks)
    dealer = Dealer()
    player = Player()
    game_play = GamePlay(player, dealer, game_deck, blackjack_multiplier)
    return game_deck, dealer, player, game_play


game_deck, dealer, player, game_play = start_game()

st.title('BlackJack Simulator')

if st.button('New hand?'):
    game_play.deal_in()


player_stats = st.empty()
player_images = st.empty()
player_hit_option = st.empty()
player_double_down_option = st.empty()
player_stand_option = st.empty()
dealer_stats = st.empty()
dealer_images = st.empty()
result = st.empty()


if 'Hit' in player.possible_actions:
    if player_hit_option.button('Hit'):
        player.player_hit(game_deck, game_play)
        if 'Hit' not in player.possible_actions:
            player_hit_option.empty()
if 'Double Down' in player.possible_actions:
    if player_double_down_option.button('Double Down'):
        player.double_down(game_deck, game_play)
        player_double_down_option.empty()
        player_hit_option.empty()
        player_stand_option.empty()
if 'Stand' in player.possible_actions:
    if player_stand_option.button('Stand'):
        player.stand(game_play)
        player_hit_option.empty()
        player_double_down_option.empty()
        player_stand_option.empty()


game_play.update()
player_stats.write(player)
player_images.image([Image.open(card.image_location)
                     for card in player.cards], width=100)
dealer_stats.write(dealer)
dealer_images.image([Image.open(card.image_location)
                     for card in dealer.cards], width=100)
result.write(game_play)
