

# Keep deck count. Add to deck class
self.deck_count = 0

if drawn_card.rank >= 2 and drawn_card.rank <= 6:
    card_counting_value = 1
elif drawn_card.rank >= 7 and drawn_card.rank <= 9:
    card_counting_value = 0
else:
    card_counting_value = -1
self.deck_count += card_counting_value


def get_hand_outcomes(self):
    hand_outcomes = {'Score 1': None , 'Score 2': None }
    for i in self.get_hand_scores():
        if len(self.cards) <= 1 :
            hand_outcomes[i] = 'Awaiting Deal'
        elif self.get_hand_scores()[i] == 21 and len(self.cards) == 2:
            hand_outcomes[i] = 'BlackJack'
        elif self.get_hand_scores()[i] > 21:
            hand_outcomes[i] = 'Bust'
        else:
            hand_outcomes[i] ='{} total'.format(self.get_hand_scores()[i])
    return hand_outcomes   