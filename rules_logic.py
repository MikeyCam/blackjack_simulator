

def rules_logic_pre_dealer(player, dealer, blackjack_multiplier):
    print("Entering rule logic pre dealer turn")
    if player.double_down == True:
        earning_multiplier = 2
    else:
        earning_multiplier = 1
    if player.best_outcome == 'Bust':
        player.ROI = -1 * earning_multiplier
        print("No need for Dealer to go. Player loses with a {} multiplier".format(
            str(player.ROI)))
        dealer_to_go = False
    elif player.best_outcome == 'Blackjack' and dealer.cards[0].rank not in [1, 10]:
        player.ROI = blackjack_multiplier
        print("Dealer has no chance to hit Blackjack. Player wins with a {} multiplier".format(
            str(blackjack_multiplier)))
        dealer_to_go = False
    else:
        dealer_to_go = True
        print("Dealer turn can proceed as normal")
    return dealer_to_go


def rules_logic_post_dealer(player, dealer):
    print("Entering rule logic post dealer turn")
    if player.double_down == True:
        earning_multiplier = 2
    else:
        earning_multiplier = 1
    if dealer.best_outcome == 'Bust':
        player.ROI = 1 * earning_multiplier
        print("Dealer busted. Player wins with a {} multiplier".format(str(player.ROI)))
    elif dealer.best_outcome == 'Blackjack' and player.best_outcome == 'Blackjack':
        player.ROI = 0
        print("Dealer and Player both have Blackjack. Player retains money with a {} multiplier".format(
            str(player.ROI)))
    elif dealer.best_outcome == 'Blackjack' and player.best_outcome != 'Blackjack':
        player.ROI = -1 * earning_multiplier
        print("Dealer has Blackjack. Player loses with a {} multiplier".format(
            str(player.ROI)))
    elif dealer.best_outcome != 'Blackjack' and player.best_outcome == 'Blackjack':
        player.ROI = 1 * earning_multiplier
        print("Player has Blackjack. Player wins with a {} multiplier".format(
            str(player.ROI)))
    elif int(dealer.best_outcome) == int(player.best_outcome):
        player.ROI = 0
        print("Dealer and Player have same score. Player retains money with a {} multiplier".format(
            str(player.ROI)))
    elif int(dealer.best_outcome) > int(player.best_outcome):
        player.ROI = -1 * earning_multiplier
        print("Dealer has {} wheras Player has {}. Player loses with a {} multiplier".format(
            str(dealer.best_outcome), str(player.best_outcome), str(player.ROI)))
    elif int(dealer.best_outcome) < int(player.best_outcome):
        player.ROI = 1 * earning_multiplier
        print("Dealer has {} wheras Player has {}. Player wins with a {} multiplier".format(
            str(dealer.best_outcome), str(player.best_outcome), str(player.ROI)))
    else:
        print("Outcome uncertain")
