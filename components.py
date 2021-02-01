import random

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

        if self.rank == 1:
            self.short_rank = 'A'
        elif self.rank == 11:
            self.short_rank = 'J'
        elif self.rank == 12:
            self.short_rank = 'Q'
        elif self.rank == 13:
            self.short_rank = 'K'
        else:
            self.short_rank = str(self.rank)

        if self.suit == 'Spades':
            self.short_suit = 'S'
        elif self.suit == 'Hearts':
            self.short_suit = 'H'
        elif self.suit == 'Clubs':
            self.short_suit = 'C'
        else:
            self.short_suit = 'D'

        self.image_location = 'static/images/{}{}.png'.format(
            self.short_rank, self.short_suit)

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
        self.cards = []
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

    def reset(self):
        self.cards.clear()
        self.hand_scores = [0, 0]
        self.best_outcome = 'Awaiting deal'


class Player(Dealer):
    def __init__(self):
        self.cards = []
        self.hand_scores = [0, 0]
        self.best_outcome = 'Awaiting deal'
        self.possible_actions = ['No deal yet']

    def __repr__(self):
        return 'Player Hand: {}, Scores: {}, Best Outcome: {}'.format(self.cards, list(set(self.hand_scores)), self.best_outcome)

    def stand(self, game_play):
        self.possible_actions = []
        game_play.commentary.append('Player is standing')

    def double_down(self, game_deck, game_play):
        self.hit(game_deck)
        game_play.commentary.append('Player is doubling down')
        self.possible_actions = []

    def player_hit(self, game_deck, game_play):
        self.hit(game_deck)
        game_play.commentary.append('Player has hit')
        self.get_possibilities(game_play)

    def get_possibilities(self, game_play):
        if self.best_outcome in ['Blackjack', 'Bust', 21]:
            self.possible_actions = []
            game_play.commentary.append('Player has no options')
        elif len(self.cards) == 2:
            self.possible_actions = ['Hit', 'Stand', 'Double Down']
            game_play.commentary.append(
                'Player can still hit, double down or stand')
        else:
            self.possible_actions = ['Hit', 'Stand']
            game_play.commentary.append('Player can still hit or stand')

    def reset(self):
        self.cards = []
        self.hand_scores = [0, 0]
        self.best_outcome = 'Awaiting deal'
        self.possible_actions = []
        self.has_doubled_down = False


class GamePlay:
    def __init__(self, player, dealer, game_deck, blackjack_multiplier):
        self.player = player
        self.dealer = dealer
        self.game_deck = game_deck
        self.blackjack_multiplier = blackjack_multiplier
        self.commentary = []

    def __repr__(self):
        return "Commentary: {}".format(self.commentary)

    def dealer_turn(self):
        self.dealer.hit(self.game_deck)
        if self.dealer.best_outcome == 'Blackjack':
            self.commentary.append('Dealer hit Blackjack')
        elif self.dealer.best_outcome == 'Bust':
            self.commentary.append('Dealer went Bust')
        elif int(self.dealer.best_outcome) < 17:
            self.commentary.append(
                'Dealer has {}, Dealer has to hit'.format(self.dealer.best_outcome))
            self.dealer_turn()
        elif int(self.dealer.best_outcome) == 17 and 1 in [card.rank for card in self.dealer.cards]:
            self.commentary.append('Dealer has a soft 17, Dealer has to hit')
            self.dealer_turn()
        else:
            self.commentary.append(
                'Dealer is proceeding with {}'.format(self.dealer.best_outcome))

    def update(self):
        if len(self.player.possible_actions) == 0:
            if self.player.best_outcome == 'Bust':
                self.commentary.append(
                    "Player busted. No need for Dealer to go. Player loses their initial bet")
            elif self.player.best_outcome == 'Blackjack' and self.dealer.cards[0].rank not in [1, 10]:
                self.commentary.append("Player has Blackjack. Dealer has no chance to hit Blackjack. Player wins {} times their initial bet".format(
                    str(self.blackjack_multiplier)))
            else:
                self.commentary.append("Dealer turn can proceed as normal")
                self.dealer_turn()
                if self.dealer.best_outcome == 'Bust':
                    self.commentary.append(
                        "Dealer busted. Player wins their initial bet")
                elif self.dealer.best_outcome == 'Blackjack' and self.player.best_outcome == 'Blackjack':
                    self.commentary.append(
                        "Dealer and Player both have Blackjack. Player retains their initial bet")
                elif self.dealer.best_outcome == 'Blackjack' and self.player.best_outcome != 'Blackjack':
                    self.commentary.append(
                        "Dealer has Blackjack. Player loses their initial bet")
                elif self.dealer.best_outcome != 'Blackjack' and self.player.best_outcome == 'Blackjack':
                    self.commentary.append("Player has Blackjack. Player wins {} times their initial bet".format(
                        str(self.blackjack_multiplier)))
                elif int(self.dealer.best_outcome) == int(self.player.best_outcome):
                    self.commentary.append(
                        "Dealer and Player have same score. Player retains their initial bet")
                elif int(self.dealer.best_outcome) > int(self.player.best_outcome):
                    self.commentary.append("Dealer has {} whereas Player has {}. Player loses their initial bet".format(
                        str(self.dealer.best_outcome), str(self.player.best_outcome)))
                else:
                    self.commentary.append("Dealer has {} whereas Player has {}. Player wins their initial bet".format(
                        str(self.dealer.best_outcome), str(self.player.best_outcome)))
        else:
            pass

    def reset(self):
        self.commentary = []

    def deal_in(self):
        self.dealer.reset()
        self.player.reset()
        self.game_deck.reset()
        self.reset()
        self.player.hit(self.game_deck)
        self.dealer.hit(self.game_deck)
        self.player.hit(self.game_deck)
        self.player.get_possibilities(self)
