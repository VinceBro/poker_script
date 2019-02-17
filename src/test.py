hand_to_value = {'2c': 2, '2d': 2, '2h': 2, '2s': 2, '3c': 3, '3d': 3, '3h': 3, '3s': 3, '4c': 4, '4d': 4, '4h': 4, '4s': 4, '5c': 5, '5d': 5, '5h': 5, '5s': 5, '6c': 6, '6d': 6, '6h': 6, '6s': 6, '7c': 7, '7d': 7, '7h': 7, '7s': 7, '8c': 8, '8d': 8, '8h': 8, '8s': 8, '9c': 9, '9d': 9, '9h': 9, '9s': 9, 'Tc': 10, 'Td': 10, 'Th': 10, 'Ts': 10, 'Jc': 11, 'Jd': 11, 'Jh': 11, 'Js': 11, 'Qc': 12, 'Qd': 12, 'Qh': 12, 'Qs': 12, 'Kc': 13, 'Kd': 13, 'Kh': 13, 'Ks': 13, 'Ac': 14, 'Ad': 14, 'Ah': 14, 'As': 14}

value_to_hand = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}




# def straight(hand):
#     suite = 0
#     cartes_valeurs = []
#     carte_sup = "1"
#     for carte in hand:
#         cartes_valeurs.append(self.hand_to_value[carte[0]])
#         if int(self.hand_to_value[carte[0]]) < carte_sup:
#             carte_sup = carte
#     cartes_valeurs = sorted(cartes_valeurs)
#     for i in range(len(cartes_valeurs)-1):
#         if suite == 3:
#             return (True, carte_sup)
#         elif cartes_valeurs[i+1] - cartes_valeurs[i] == 1:
#             suite += 1
#         else:
#             suite = 0
#     return False


def straight(hand):
    suite = 0
    cartes_valeurs = []
    carte_sup = ""
    for carte in hand:
        print(carte[0])
        hand_to_value[carte]
        cartes_valeurs.append(hand_to_value[carte])
        if carte_sup == "":
            carte_sup = carte
        if int(hand_to_value[carte]) > int(hand_to_value[carte_sup]):
            carte_sup = carte
    cartes_valeurs = sorted(cartes_valeurs)
    for i in range(len(cartes_valeurs)-1):
        if suite == 3:
            return (True, carte_sup)
        elif cartes_valeurs[i+1] - cartes_valeurs[i] == 1:
            suite += 1
        else:
            suite = 0
    return False

straight(['2s','3s','4s','5s','6s'])
