import numpy as np
import random as r
import json, requests, pickle, datetime, sys, itertools, copy, time

class Cards(object):
    def __init__(self):
        self.hand = []
        self.community = []
        self.SUITS = 'cdhs'
        self.RANKS = '23456789TJQKA'
        self.deck = list(''.join(card) for card in itertools.product(self.RANKS, self.SUITS))
        self.hand_to_value = {'2c': 2, '2d': 2, '2h': 2, '2s': 2, '3c': 3, '3d': 3, '3h': 3, '3s': 3,
        '4c': 4, '4d': 4, '4h': 4, '4s': 4, '5c': 5, '5d': 5, '5h': 5, '5s': 5, '6c': 6, '6d': 6,
        '6h': 6, '6s': 6, '7c': 7, '7d': 7, '7h': 7, '7s': 7, '8c': 8, '8d': 8, '8h': 8, '8s': 8,
        '9c': 9, '9d': 9, '9h': 9, '9s': 9, 'Tc': 10, 'Td': 10, 'Th': 10, 'Ts': 10, 'Jc': 11,
        'Jd': 11, 'Jh': 11, 'Js': 11, 'Qc': 12, 'Qd': 12, 'Qh': 12, 'Qs': 12, 'Kc': 13, 'Kd': 13,
        'Kh': 13, 'Ks': 13, 'Ac': 14, 'Ad': 14, 'Ah': 14, 'As': 14}

        self.value_to_hand = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
    def __str__(self):
        return self.deck


class Hands(Cards):
    def __init__(self):
        super().__init__()
    def convert_to_value(self, hand):
        if isinstance(hand, set):
            return hand
        if isinstance(hand[0], str):
            return sorted([self.hand_to_value[carte] for carte in hand])
        else:
            return hand


    def roy_flush(self, hand):
        temp_hand = copy.copy(hand)
        cartes_valeurs = self.convert_to_value(hand)
        scartes = set(cartes_valeurs)
        try:
            if scartes.intersection({14, 13, 12, 11, 10}) == {14, 13, 12, 11, 10}:
                for carte in hand:
                    if self.hand_to_value[carte] != 14 or self.hand_to_value[carte]!= 13 or self.hand_to_value[carte] != 12 or self.hand_to_value[carte] != 11 or self.hand_to_value[carte] != 10:
                        temp_hand.remove(carte)
                if self.flush(temp_hand):
                    return True
        except TypeError:
            return False

        return False

    def str_flush(self, hand):
        flush = self.flush(hand)
        if flush[0]:
            str8 = self.straight(flush[1])
            if str8[0]:
                return (True, str8[1])
        return(False, None)

    def four_of_k(self, hand):
        counter = 1
        current = 0
        for i in self.convert_to_value(hand):
            if current != i:
                current = i
                counter = 1
            elif current == i:
                counter += 1
            if counter >= 4:
                return (True, current)
        return (False, None)

    #returns (True, three_of_k, pair)
    ###PAS ENCORE TESTÉ CETTE FONCTION LA
    def full_house(self, hand):
        temp_hand = copy.copy(hand)
        three = self.three_of_k(hand)
        if three[0]:
            temp_hand = self.convert_to_value(temp_hand)
            i = 0
            while i<len(temp_hand):
                # print(temp_hand[i])
                if temp_hand[i] == three[1]:
                    temp_hand.remove(temp_hand[i])
                i+=1
            pair = self.pair(temp_hand)
            if pair[0]:
                return(True, three[1], pair[1])
        return(False, None)
    # def full_house(self, hand):
    #     temp_hand = copy.copy(hand)
    #     three = self.three_of_k(hand)
    #
    #     if three[0]:
    #         for carte in hand:
    #             if carte[0] == three[1]:
    #                 temp_hand.remove(carte)
    #         pair = self.pair(temp_hand)
    #         if pair[0]:
    #             return(True, three[1], pair[1])
    #
    #     return(False, None)


    ###PAS ENCORE TESTÉ CETTE FONCTION LA
    def flush(self, hand):
        currenth = []
        currentc = []
        currents = []
        currentd = []
        for i in hand:
            if i[1] == 'h':
                currenth.append(self.hand_to_value[i])
            if i[1] == 'c':
                currentc.append(self.hand_to_value[i])
            if i[1] == 's':
                currents.append(self.hand_to_value[i])
            if i[1] == 'd':
                currentd.append(self.hand_to_value[i])
        if len(currentd) >= 5:
            while len(currentd) > 5:
                currentd.pop(0)
            return (True,sorted(currentd))
        elif len(currents) >= 5:
            while len(currents) > 5:
                currents.pop(0)
            return (True,sorted(currents))
        elif len(currentc) >= 5:
            while len(currentc) > 5:
                currentc.pop(0)
            return (True,sorted(currentc))
        elif len(currenth) >= 5:
            while len(currenth) > 5:
                currenth.pop(0)
            return (True,sorted(currenth))
        return (False, None)

    def straight(self, hand):
        suite = 0
        cartes_valeurs = self.convert_to_value(hand)
        str8 = []
        scartes = set(cartes_valeurs)


        #Pour le cas unique A 2 3 4 5 (6) (7)
        if scartes.intersection({14, 2, 3, 4, 5, 6, 7}) == {14, 2, 3, 4, 5, 6, 7}:
            return(True, 7)
        elif scartes.intersection({14, 2, 3, 4, 5, 6}) == {14, 2, 3, 4, 5, 6}:
            return(True, 6)
        elif scartes.intersection({14, 2, 3, 4, 5}) == {14, 2, 3, 4, 5}:
            return(True, 5)

        for i in list(range(len(cartes_valeurs)))[1:]:
            if suite >= 4:
                return (True, str8[-1])
            if cartes_valeurs[i] - cartes_valeurs[i-1] == 1:
                if str8 == []:
                    str8.append(cartes_valeurs[i-1])
                str8.append(cartes_valeurs[i])
                suite += 1
            else:
                str8 = []
                suite = 0
        return (False, None)

    def three_of_k(self, hand):
        counter = 1
        current = " "
        for i in self.convert_to_value(hand):
            if current != i:
                current = i
                counter = 1
            elif current == i:
                counter += 1
            if counter >= 3:
                return (True, current)
        return (False, None)

    ###PAS TESTÉ CETTE FONCTION LA ENCORE
    def two_pair(self, hand):
        reponse = self.pair(hand)
        temp_hand = self.convert_to_value(copy.copy(hand))
        for i in temp_hand:
            if i == reponse[1]:
                temp_hand.remove(i)
        reponse2 = self.pair(temp_hand)
        if reponse2[0]:
            return (True,reponse[1], reponse2[1])
        return (False, None)


    def pair(self, hand):
        current = " "
        vpair = 0
        hand = self.convert_to_value(hand)
        for i in hand:
            if current != i:
                current = i
            elif current == i:
                if i > vpair:
                    vpair = i
        if vpair != 0:
            return (True, vpair)
        return (False, None)

    def high_card(self, hand):
        temp_hand = self.convert_to_value(hand)
        return (True, temp_hand[(len(temp_hand)%5):(len(temp_hand))])

class Odds(Hands):
    def __init__(self):
        super().__init__()

        #TODO prends self.deck dans cards et enleve les cartes dans les mains
        #du joueur et les cartes dans community

        self.poss_op_hands = []
        self.played = []
        self.opplayed = []
        self.all_4_cards = []
        self.ahead = 0
        self.tie = 0
        self.behind = 0
        self.opHand = []
        self.current_deck = []
        self.opponents = 1
        self.cunter = 0

    # def create_all_4_cards(self):
    #     counter = 0
    #     self.all_4_cards = list(itertools.combinations(self.current_deck, 4))
    #     for i in self.all_4_cards:
    #         allo = []
    #         allo.append(itertools.permutations(list(i),4))
    #         yield allo
    def create_all_4_cards_for_approx(self, hand):
        counter = 0
        for i in itertools.combinations(self.current_deck, 2):
            fake_deck = copy.copy(self.current_deck)
            fake_deck.remove(i[0])
            fake_deck.remove(i[1])
            for j in itertools.combinations(fake_deck, 2):
                counter += 1
                yield i + j


    def create_all_4_cards(self, hand):
        counter = 0
        fake_deck = copy.copy(self.current_deck)
        fake_deck.remove(hand[0])
        fake_deck.remove(hand[1])
        length = len(fake_deck)
        for i in range(length):
            for j in range(i + 1, length):
                bonheur = []
                bonheur.append(self.current_deck[i])
                bonheur.append(self.current_deck[j])
                yield bonheur

        ### Pour afficher toutes les possibilités des 4 cartes(1070190 possibilités)
        # for i in itertools.combinations(self.current_deck, 2):
        #     fake_deck = copy.copy(self.current_deck)
        #     fake_deck.remove(i[0])
        #     fake_deck.remove(i[1])
        #     for j in itertools.combinations(fake_deck, 2):
        #         counter += 1
        #         yield i + j
        # print(counter)
    def HandPotentialApproximation(self):
        ahead = behind = tied = 0
        self.update_deck()
        counter = 0
        for i in self.create_all_4_cards_for_approx(self.played):
            counter +=1
            # print(list(self.played))
            i = list(i)
            main1 = list(self.played)
            main1.append(i[2])
            main1.append(i[3])
            main2 = self.community+i
            # print(main1)
            # print(main2)
            output = self.compare(main1, main2)
            if output[0] == "Win":
                ahead += 1
            elif output[0] == "Loss":
                behind += 1
            else:
                tied += 1
        print('ahead:', ahead,'tied:', tied,'behind:', behind)
        print('counter: ', counter)
        allo = ((ahead+tied/2)/(ahead + tied + behind))*100
        print(str(allo)+'% chances of winning')
        return(((ahead+tied/2)/(ahead + tied + behind))*100)


    def HandPotential(self):
        """calcul de 178,365 probabilitées après le flop pour prédire le nombre de
        mains qui gagneront/perderont de la valeur après le turn et le river"""
        
        cdef int ahead, behind, tied, i, j, x, length
        cdef int HP[3][3]
        cdef int HP_total[1][3]
        # self.calculate()
        # prob_array_calculate[0,0] = self.ahead
        # prob_array_calculate[1,1] = self.tied
        # prob_array_calculate[2,2] = self.behind
        self.update_deck()
        self.played = self.hand + self.community
        ahead = 0
        behind = 2
        tied = 1
        length = len(self.current_deck)
        # print(length)
        # print(len(self.all_4_cards))
        print("we're in")
        for i in range(length):
            for j in range(i + 1, length):
                # print(i)
                self.cunter += 1
                bonheur = []
                bonheur.append(self.current_deck[i])
                bonheur.append(self.current_deck[j])
                joie = bonheur
                bonheur += self.community
                ### bonheur est devenu
                output = self.compare(self.played, bonheur)

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
                for x in self.create_all_4_cards(joie):
                    self.cunter += 1
                    adjusted_rank = self.compare(self.played + x, bonheur + x)
                    if str(adjusted_rank[0]) == "Loss":
                        HP[index,ahead] += 1
                    elif str(adjusted_rank[0]) == "Tie" and index == 2:
                        HP[index,tied] += 1
                    else:
                        HP[index,behind] += 1

        Ppot = (HP[behind, ahead]+(HP[behind, tied])/2 + (HP[tied,ahead])/2)/(HP_total[0, behind]+HP_total[0, tied])
        Npot = (HP[ahead,behind]+HP[tied,behind]/2 + HP[ahead,tied]/2)/(HP_total[0, ahead]+HP_total[0, tied])
        print(self.cunter)
        return (Ppot, Npot)



    #Prends en entrée la main au complet
    def calculate(self, hand, community):
        """calcul de 1081 probabilités en fonction du nombre d'adversaires
        , des cartes dans les mains du joueur et dans les mains des adversaires"""
        self.ahead = self.tied = self.behind = 0
        self.update_deck()
        length = len(self.current_deck)
        for i in range(length):
            for j in range(i + 1, length):
                self.cunter += 1
                bonheur = []
                bonheur.append(self.current_deck[i])
                bonheur.append(self.current_deck[j])
                bonheur += community
                output = self.compare(hand + community, bonheur)
                if output[0] == "Win":
                    self.ahead += 1
                elif output[0] == "Loss":
                    self.behind += 1
                else:
                    self.tied += 1

        return(((self.ahead+self.tied/2)/(self.ahead + self.tied + self.behind))**self.opponents)
                #self.poss_op_hands.append((self.current_deck[i], self.current_deck[j]))
        print(len(self.poss_op_hands))
        print(self.poss_op_hands)


    ###FOR TEST PURPOSES
    cpdef double test_calculate(self):
        start = time.time()
        self.played = []
        self.cunter = 0
        self.opponents = r.choice([1, 2, 3, 4, 5, 6, 7])
        self.create_random_board()
        self.create_random_hand()
        self.played = self.hand + self.community
        ##À vérifier: ajusted_odds = (self.calculate(self.played) * 100)**self.opponents
        print("Your hand : " + str(self.hand) + "  Community cards : " + str(self.community))
        print("# of opponents : " +  str(self.opponents))
        print("\n")
        print("Odds of winning : " + str(round(self.calculate(self.hand, self.community) * 100, 2)) + "%")

        # print("Ajusted odds of winning(# players) : " + str(float(round((self.calculate(self.played) * 100))**self.opponents), 2) + "%")
        print("Wins : " + str(self.ahead) + "    Losses : " + str(self.behind) + "    Ties : " + str(self.tied))
        print("Iterations : " + str(self.cunter))
        end = time.time()
        print("Execution time : " + str(round(end-start,3)) + 's')
        print('_' * 55)



    def test_function(self, hand):
        wait = ""
        dict = {"hand" : [], "stats": {"roy_flush": self.roy_flush(hand),"str_flush": self.str_flush(hand), "four_of_k" : self.four_of_k(hand), "full_house": self.full_house(hand), "flush": self.flush(hand), "straight" : self.straight(hand), "three_of_k": self.three_of_k(hand), "two_pair": self.two_pair(hand), "pair" : self.pair(hand) }}
        for function in dict["stats"]:
            ## prochaine ligne jcomprends pas pk est la
            #dict["stats"][function]
            print("These are the current hands: " + str(hand1))
            print("For function: " + function)
            print("Current output is: " + str(dict["stats"][function]))
            wait = input("Press enter to continue")

    def test_compare(self):
        self.create_random_board()
        self.create_random_hand()
        self.played = self.hand + self.community
        print("This is our hand: " + str(self.hand))
        self.create_random_hand()
        self.opplayed = self.hand + self.community
        print("This is not our hand (opponent): " + str(self.hand))
        print("These are the community cards : " + str(self.community))
        rep = self.compare(self.played, self.opplayed)
        print(rep)
        #print("Output of the round is: " + self.compare(ourhand, ophand))
        if rep[1] == 9:
            print("Output if the round is: " + rep[0] + " with Royal Flush")
        elif rep[1] == 8:
            print("Output if the round is: " + rep[0] + " with Straight flush")
        elif rep[1] == 7:
            print("Output if the round is: " + rep[0] + " with Four of a kind")
        elif rep[1] == 6:
            print("Output if the round is: " + rep[0] + " with Full House")
        elif rep[1] == 5:
            print("Output if the round is: " + rep[0] + " with Flush")
        elif rep[1] == 4:
            print("Output if the round is: " + rep[0] + " with Straight")
        elif rep[1] == 3:
            print("Output if the round is: " + rep[0] + " with Three of a kind")
        elif rep[1] == 2:
            print("Output if the round is: " + rep[0] + " with Two pair")
        elif rep[1] == 1:
            print("Output if the round is: " + rep[0] + " with Pair")
        elif rep[1] == 0:
            print("Output if the round is: " + rep[0] + " with High card")
        else:
            print("On a un bug ici mon ami")


    def create_random_hand(self):
        ret_hand = []
        for i in range(2):
            choice = r.choice(self.current_deck)
            ret_hand.append(choice)
            self.current_deck.remove(choice)
        self.hand = ret_hand

    ###FOR TEST PURPOSES
    def create_random_board(self):
        self.current_deck = copy.copy(self.deck)
        ret_hand = []
        possible_length = [3, 4, 5]
        for i in range(r.choice(possible_length)):
            choice = r.choice(self.current_deck)
            ret_hand.append(choice)
            self.current_deck.remove(choice)
        self.community = ret_hand



    def update_deck(self):
        # self.current_deck = [x for x in self.deck if not in self.played]
        self.current_deck = copy.copy(self.deck)
        self.played = set(self.played)
        self.current_deck = list(filter(lambda x: x not in self.played, self.current_deck))

    def Rank(self, hand):
        rep = self.roy_flush(hand)
        if rep:
            return (9, None)
        rep = self.str_flush(hand)
        if rep[0]:
            return (8, rep[1])
        rep = self.four_of_k(hand)
        if rep[0]:
            return (7, rep[1])
        rep = self.full_house(hand)
        if rep[0]:
            return (6, rep[1], rep[2])
        rep = self.flush(hand)
        if rep[0]:
            return (5, rep[1])
        rep = self.straight(hand)
        if rep[0]:
            return (4, rep[1])
        rep = self.three_of_k(hand)
        if rep[0]:
            return (3, rep[1])
        rep = self.two_pair(hand)
        if rep[0]:
            return (2, rep[1], rep[2])
        rep = self.pair(hand)
        if rep[0]:
            return (1, rep[1])
        rep = self.high_card(hand)
        return (0, rep[1])

    ## reste four of a kind, flush, three of a kind, two pair
    def compare(self, ourHand, opponentHand):
        length = 0
        ourHand_c = self.convert_to_value(ourHand)
        opHand_c = self.convert_to_value(opponentHand)
        set_ourHand = set(ourHand_c)
        set_opHand = set(opHand_c)
        # self.cunter += 1
        ourRank = self.Rank(ourHand)
        opponentRank = self.Rank(opponentHand)
        win = "Win"
        loss = "Loss"
        tie = "Tie"
        if ourRank[0] > opponentRank[0]:
            return (win, ourRank[0])
        elif ourRank[0] < opponentRank[0]:
            return (loss, opponentRank[0])
        else:
            ##royal flush
            if ourRank[0] == 9:
                return (tie, ourRank[0])

            ## straigth flush
            elif ourRank[0] == 8:
                if ourRank[1] > opponentRank[1]:
                    return (win, ourRank[0])
                elif ourRank[1] < opponentRank[1]:
                    return (loss, opponentRank[0])
                else:
                    return (tie, ourRank[0])
            ##four of a kind
            elif ourRank[0] == 7:
                if ourRank[1] > opponentRank[1]:
                    return (win, ourRank[0])
                elif ourRank[1] < opponentRank[1]:
                    return (loss, opponentRank[0])
                else:
                    set_ourHand.remove(ourRank[1])
                    set_opHand.remove(opponentRank[1])
                    list_ourHand = list(set_ourHand)
                    list_opHand = list(set_opHand)
                    list_ourHand.sort()
                    list_opHand.sort()
                    if list_ourHand[-1] > list_opHand[-1]:
                        return (win, ourRank[0])
                    elif list_ourHand[-1] < list_opHand[-1]:
                        return (loss, opponentRank[0])
                    else:
                        return (tie, ourRank[0])

                    ##### set des deux mains, on check pour la carte la plus forte,
                    ## si la carte la plus forte est le 4 of a kind, on va a l'index avant
                    ## et on sait que c'est la carte la plus forte
                    ### CAS 4 CARTES PAREILLES SUR LE BOARD
            ##full house
            elif ourRank[0] == 6:
                if ourRank[1] > opponentRank[1]:
                    return (win, ourRank[0])
                elif ourRank[1] < opponentRank[1]:
                    return (loss, opponentRank[0])
                else:
                    if ourRank[2] > opponentRank[2]:
                        return (win, ourRank[0])
                    elif ourRank[2] < opponentRank[2]:
                        return (loss, opponentRank[0])
                    else:
                        return (tie, ourRank[0])
            ##flush
            elif ourRank[0] == 5:
                ourFlush = ourRank[1]
                opponentFlush = opponentRank[1]

                for i in range(5)[::-1]:
                    if ourFlush[i] > opponentFlush[i]:
                        return (win, ourRank[0])
                    elif ourFlush[i] < opponentFlush[i]:
                        return (loss, ourRank[0])
                return (tie, ourRank[0])
                # funny_list = [carte[0] for carte in ourHand if carte[1] == ourRank[1]]
                # angry_list = [carte[0] for carte in opponentHand if carte[1] == opponentRank[1]]



                # for carte in ourHand:
                #     if carte[1] == ourRank[1]:
                #         funny_list.append(carte[0])
                #     else:
                #         continue
                # for carte in opponentHand:
                #     if carte[1] == opponentRank[1]:
                #         angry_list.append(carte[0])
                #     else:
                #         continue
                # while len(angry_list)>5:
                # input("s")
                #     angry_list.pop()
                # while len(funny_list)>5:
                #     funny_list.pop()
                # angry_list = sorted(angry_list)
                # funny_list = sorted(funny_list)
                # for i in range(4):
                #     if funny_list[4-i]>angry_list[4-i]:
                #         return (win, ourRank[0])
                #     elif funny_list[4-i]<angry_list[4-i]:
                #         return (loss, opponentRank[0])
                #     else:
                #         continue
                # return (tie, ourRank[0])

            ##straight
            elif ourRank[0] == 4:
                if ourRank[1] > opponentRank[1]:
                    return (win, ourRank[0])
                elif ourRank[1] < opponentRank[1]:
                    return (loss, opponentRank[0])
                else:
                    return (tie, ourRank[0])
            ##three of a kind
            elif ourRank[0] == 3:
                if ourRank[1] > opponentRank[1]:
                    return (win, ourRank[0])
                elif ourRank[1] < opponentRank[1]:
                    return (loss, opponentRank[0])
                else:
                    set_ourHand.remove(ourRank[1])
                    set_opHand.remove(opponentRank[1])
                    list_ourHand = list(set_ourHand)
                    list_opHand = list(set_opHand)
                    list_ourHand.sort()
                    list_opHand.sort()

                    ## Pourrait être changé pour un for
                    if list_ourHand[-1] > list_opHand[-1]:
                        return (win, ourRank[0])
                    elif list_ourHand[-1] < list_opHand[-1]:
                        return (loss, opponentRank[0])
                    else:
                        if list_ourHand[-2] > list_opHand[-2]:
                            return (win, ourRank[0])
                        elif list_ourHand[-2] < list_opHand[-2]:
                            return (loss, opponentRank[0])
                        else:
                            return (tie, ourRank[0])

                pass
            ##two_pair
            elif ourRank[0] == 2:
                # for i in range(3)[:1]:
                for i in range(3)[1:]:
                    ##probleme ici
                    if ourRank[i] > opponentRank[i]:
                        return (win, ourRank[0])
                    elif ourRank[i] < opponentRank[i]:
                        return (loss, opponentRank[0])
                    else:
                        continue
                    set_ourHand.remove(ourRank[i])
                    set_opHand.remove(opponentRank[i])

                #si les 2 cartes de la paire sont dans la main

                #ca chie ici tu peux pas index des sets!!

                list_ophand = list(set_opHand)
                list_ourhand = list(set_ourHand)

                for i in range(3):
                    if list_ourhand[i] > list_ophand[i]:
                        return (win, ourRank[0])
                    elif list_ourhand[i] < list_ophand[i]:
                        return (loss, opponentRank[0])
                    else:
                        continue
                return (tie, ourRank[0])
            ##pair
            elif ourRank[0] == 1:
                if ourRank[1] > opponentRank[1]:
                    return (win, ourRank[0])
                elif ourRank[1] < opponentRank[1]:
                    return (loss, opponentRank[0])
                else:
                    set_ourHand.remove(ourRank[1])
                    set_opHand.remove(opponentRank[1])
                    list_ourHand = list(sorted(set_ourHand))
                    list_opHand = list(sorted(set_opHand))
                    # list_ourHand.sort()
                    # list_opHand.sort()
                    length = len(list_ourHand) - 1
                    for i in range(length):
                        #import pdb; pdb.set_trace()
                        ###ya un probleme ici
                        if list_ourHand[length-i] > list_opHand[length-i]:
                            return (win, ourRank[0])
                        elif list_ourHand[length-i] < list_opHand[length-i]:
                            return (loss, opponentRank[0])
                        else:
                            continue
                    return (tie, ourRank[0])
            ##high card
            elif ourRank[0] == 0:
                for i in list(range(len(ourHand)))[::-1]:
                    if ourHand_c[i] > opHand_c[i]:
                        return (win, ourRank[0])
                    elif ourHand_c[i] < opHand_c[i]:
                        return (loss, opponentRank[0])
                    else:
                        continue
                return (tie, ourRank[0])




    #placé les fonctions dans l'ordre en fonction de leur force
    ###PAS ENCORE TESTÉ CELLE LA
    
