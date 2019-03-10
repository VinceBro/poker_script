import itertools
import copy
import random as r
import numpy as np
from algorithm import *


SUITS = 'cdhs'
RANKS = '23456789TJQKA'

deck = list(''.join(card) for card in itertools.product(RANKS, SUITS))
test_board = []
temp_hand = []

hand_to_value = {'2c': 2, '2d': 2, '2h': 2, '2s': 2, '3c': 3, '3d': 3, '3h': 3, '3s': 3,
'4c': 4, '4d': 4, '4h': 4, '4s': 4, '5c': 5, '5d': 5, '5h': 5, '5s': 5, '6c': 6, '6d': 6,
'6h': 6, '6s': 6, '7c': 7, '7d': 7, '7h': 7, '7s': 7, '8c': 8, '8d': 8, '8h': 8, '8s': 8,
'9c': 9, '9d': 9, '9h': 9, '9s': 9, 'Tc': 10, 'Td': 10, 'Th': 10, 'Ts': 10, 'Jc': 11,
'Jd': 11, 'Jh': 11, 'Js': 11, 'Qc': 12, 'Qd': 12, 'Qh': 12, 'Qs': 12, 'Kc': 13, 'Kd': 13,
'Kh': 13, 'Ks': 13, 'Ac': 14, 'Ad': 14, 'Ah': 14, 'As': 14}

def HandPotential(hand):
    """calcul de 178,365 probabilitées après le flop pour prédire le nombre de
    mains qui gagneront/perderont de la valeur après le turn et le river"""
    HP_total = np.zeros((1,3))
    HP = np.zeros((3,3))
    # odds.calculate()
    # prob_array_calculate[0,0] = odds.ahead
    # prob_array_calculate[1,1] = odds.tied
    # prob_array_calculate[2,2] = odds.behind
    odds.update_deck()
    print(odds.hand)
    print(odds.community)
    odds.played = odds.hand + odds.community
    odds.create_all_4_cards()
    ahead = 0
    behind = 2
    tied = 1
    length = len(odds.current_deck)
    # print(length)
    # print(len(odds.all_4_cards))
    for i in range(length):
        for j in range(i + 1, length):
            odds.cunter += 1
            bonheur = []
            bonheur.append(odds.current_deck[i])
            bonheur.append(odds.current_deck[j])
            bonheur += odds.community
            output = odds.compare(hand, bonheur)

            ## win = 0, loss = 2, tie = 1
            if output[0] == "Win":
                index = ahead
            elif output[0] == "Loss":
                index = behind
            else:
                index = tied

            HP_total[0, index] += 1
            # print(HP_total)

        #final 5 cards!!!
            for k in range(len(odds.all_4_cards)):
                adjusted_rank = odds.compare(list(odds.played)+list(odds.all_4_cards[k]), list(odds.community)+list(odds.all_4_cards[k]))
                if str(adjusted_rank[0]) == "Loss":
                    HP[index,ahead] += 1
                elif str(adjusted_rank[0]) == "Tie" and index == 2:
                    HP[index,tied] += 1
                else:
                    HP[index,behind] += 1

    # Ppot = (HP[behind, ahead]+(HP[behind, tied])/2 + (HP[tied,ahead])/2)/(HP_total[behind]+HP_total[tied])
    # Npot = (HP[ahead,behind]+HP[tied,behind]/2 + HP[ahead,tied]/2)/(HP_total[ahead]+HP_total[tied])
    # return (Ppot, Npot)



if __name__ == '__main__':
    odds = Odds('romi')
    odds.community = ['4s','6s','8d']
    odds.hand = ['Jd','Ts']
    odds.played = odds.hand + odds.community
    allo = ['2d','2h']
    odds.update_deck()
    # print(odds.current_deck)

    # for i in odds.create_all_4_cards_for_approx(allo):
    #     print(i)
    start = time.time()
    odds.HandPotentialApproximation()


    # for i in odds.create_all_4_cards():
    #     print(next(i))
        # for j in i:
        #     print(next(j))
    # print(odds.HandPotential())
    end = time.time()
    print(end-start)
