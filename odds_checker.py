from itertools import combinations 

number_of_decks = 6 

options = [1,2,3,4,5,6,7,8,9,10,10,10,10] * 4
deck = options * 6


hand_1 = [2,3]
hand_2 = [1]
for x in hand_1:
    deck.remove(x)
for x in hand_2:
    deck.remove(x)

#print(deck)

max_hand_length = 3
for i in range(1,max_hand_length):
    (list(combinations(deck,i)))




