import itertools
import copy
import random as r

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
from algorithm import *

# def pair(hand):
#     ### à checker, doit retourner la carte de la paire, et non la carte la plus haute autre que la paire
#     current = " "
#     vpair = 0
#     for i in hand:
#         if current != i[0]:
#             current = i[0]
#         elif current == i[0]:
#             if hand_to_value[i] > vpair:
#                 vpair = hand_to_value[i]
#     if vpair != 0:
#         # return (True, self.value_to_hand[vpair])
#         return (True, vpair)
#     return (False, None)
#
# def two_pair(hand):
#     temp_hand = copy.copy(hand)
#     p1 = pair(hand)
#     try:
#         if p1[0]:
#             for i in hand:
#
#                 if int(i[0]) == int(p1[1]):
#                     temp_hand.remove(i)
#         print(temp_hand)
#         p2 = pair(temp_hand)
#         if p2[0]:
#             return (True, p1[1], p2[1])
#     except TypeError:
#         return (False, None)
#     return (False, None)

def high_card(hand):
    temp_hand = odds.convert_to_value(hand)
    return (True, temp_hand[(len(temp_hand)%5):(len(temp_hand))])



if __name__ == '__main__':
    odds = Odds('romi')
    main1 = ['4s','6s','8d','Td','As']
    main2 = ['4s','6s','8d','Jd','Ts']
    print(high_card(main1))
    print(high_card(main2))
    print('\n')
    print(odds.compare(main1, main2))
