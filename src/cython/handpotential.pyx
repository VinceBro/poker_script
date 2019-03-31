from algorithm import *


def HandPotential(hand, community):
    """calcul de 178,365 probabilitées après le flop pour prédire le nombre de
    mains qui gagneront/perderont de la valeur après le turn et le river"""
    # HP_total = np.zeros((1,3))
    # HP = np.zeros((3,3))
    odds = Odds()
    cdef int ahead, behind, tied, i, j, x, length
    cdef float Ppot, Npot
    cdef int HP[3][3]
    cdef int HP_total[1][3]

    # odds.calculate()
    # prob_array_calculate[0,0] = odds.ahead
    # prob_array_calculate[1,1] = odds.tied
    # prob_array_calculate[2,2] = odds.behind
    odds.hand = hand
    odds.community = community
    odds.update_deck()
    odds.played = hand + community
    ahead = 0
    tied = 1
    behind = 2
    length = len(odds.current_deck)
    # print(length)
    # print(len(odds.all_4_cards))
    print("we're in")
    for i in range(length):
        for j in range(i + 1, length):
            # print(i)
            odds.cunter += 1
            bonheur = []
            bonheur.append(odds.current_deck[i])
            bonheur.append(odds.current_deck[j])
            joie = bonheur
            bonheur += odds.community
            ### bonheur est devenu
            output = odds.compare(odds.played, bonheur)

            ## win = 0, loss = 2, tie = 1
            if output[0] == "Win":
                index = ahead
            elif output[0] == "Loss":
                index = behind
            else:
                index = tied

            HP_total[0, index] += 1
            # print(HP_total)

            ### POUR FLOP
            for x in odds.create_all_4_cards(joie):
                odds.cunter += 1
                adjusted_rank = odds.compare(odds.played + x, bonheur + x)
                if str(adjusted_rank[0]) == "Loss":
                    HP[index,ahead] += 1
                elif str(adjusted_rank[0]) == "Tie" and index == 2:
                    HP[index,tied] += 1
                else:
                    HP[index,behind] += 1

    Ppot = (HP[behind, ahead]+(HP[behind, tied])/2 + (HP[tied,ahead])/2)/(HP_total[0, behind]+HP_total[0, tied])
    Npot = (HP[ahead,behind]+HP[tied,behind]/2 + HP[ahead,tied]/2)/(HP_total[0, ahead]+HP_total[0, tied])
    print(odds.cunter)
    return (Ppot, Npot)
