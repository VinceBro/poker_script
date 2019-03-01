from script import *
import random as r



class Odds(Manager):
    def __init__(self, username):
        super().__init__(username)

        #TODO prends self.deck dans cards et enleve les cartes dans les mains
        #du joueur et les cartes dans community

        self.possible = r.choice(self.deck)
        self.played = self.hand + self.community
        self.testing_dict = {"hand" : [], "stats": {"roy_flush": [],"str_flush": [], "four_of_k" : [], "full_house": [], "flush": [], "straight" : [], "three_of_k": [], "two_pair": [], "pair" : [] }}
        self.ahead = 0
        self.tie = 0
        self.cunter = 0
        self.opHand = []
        self.test_board = []

    def Rank(self, hand):
        rep = self.royal_flush(hand)
        if rep[0]:
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
            return (2, rep[1])
        rep = self.pair(hand)
        if rep[0]:
            return (1, rep[1])
        rep = self.high_card(hand)
        return (0, rep[0])

    ## reste four of a kind, flush, three of a kind, two pair
    def compare(self, ourHand, opponentHand):
        ourHand_c = self.convert_to_value(ourHand)
        opHand_c = self.convert_to_value(opponentHand)
        set_ourHand = set(ourHand_c)
        set_ophand = set(opHand_c)
        self.cunter += 1
        ourRank = self.Rank(ourHand)
        opponentRank = self.Rank(opponentHand)
        win = "Win"
        loss = "Loss"
        tie = "Tie"
        # if ourRank[0] > opRank[0]:
        #     return win
        # elif ourRank[0] < opRank[0]:
        #     return loss
        # else:
        if ourRank[0] > opponentRank[0]:
            return win
        elif ourRank[0] < opponentRank[0]:
            return loss
        else:

            ##royal flush
            if ourRank[0] == 9:
                return tie

            ## straigth flush
            elif ourRank[0] == 8:
                if ourRank[1] > opponentRank[1]:
                    return win
                elif ourRank[1] < opponentRank[1]:
                    return loss
                else:
                    return tie
            ##four of a kind
            elif ourRank[0] == 7:
                if ourRank[1] > opponentRank[1]:
                    return win
                elif ourRank[1] < opponentRank[1]:
                    return loss
                else:
                    set_ourHand.remove(ourRank[1])
                    set_ophand.remove(opponentRank[1])
                    if set_ourHand[-1] > set_ophand[-1]:
                        return win
                    elif set_ourHand[-1] < set_ophand[-1]:
                        return loss
                    else:
                        return tie

                    ##### set des deux mains, on check pour la carte la plus forte,
                    ## si la carte la plus forte est le 4 of a kind, on va a l'index avant
                    ## et on sait que c'est la carte la plus forte
                    ### CAS 4 CARTES PAREILLES SUR LE BOARD
            ##full house
            elif ourRank[0] == 6:
                if ourRank[1] > opponentRank[1]:
                    return win
                elif ourRank[1] < opponentRank[1]:
                    return loss
                else:
                    if ourRank[2] > opponentRank[2]:
                        return win
                    elif ourRank[2] < opponentRank[2]:
                        return loss
                    else:
                        return tie
            ##flush
            elif ourRank[0] == 5:
                funny_list = []
                angry_list = []
                for carte in ourHand:
                    if carte[1] == ourRank[1]:
                        funny_list.append(carte[0])
                    else:
                        continue
                for carte in opponentHand:
                    if carte[1] == opponentRank[1]:
                        angry.append(carte[0])
                    else:
                        continue
                while len(angry_list)>5:
                    angry_list.pop()
                while len(funny_list)>5:
                    funny_list.pop()
                angry_list = sorted(angry_list)
                funny_list = sorted(funny_list)
                for i in range(4):
                    if funny_list[4-i]>angry_list[4-i]:
                        return win
                    elif funny_list[4-i]<angry_list[4-i]:
                        return loss
                    else:
                        continue
                return tie

            ##straight
            elif ourRank[0] == 4:
                if ourRank[1] > opponentRank[1]:
                    return win
                elif ourRank[1] < opponentRank[1]:
                    return loss
                else:
                    return tie
            ##three of a kind
            elif ourRank[0] == 3:
                if ourRank[1] > opponentRank[1]:
                    return win
                elif ourRank[1] < opponentRank[1]:
                    return loss
                else:
                    set_ourHand.remove(ourRank[1])
                    set_ophand.remove(opponentRank[1])

                    ## Pourrait être changé pour un for
                    if set_ourHand[-1] > set_ophand[-1]:
                        return win
                    elif set_ourHand[-1] < set_ophand[-1]:
                        return loss
                    else:
                        if set_ourHand[-2] > set_ophand[-2]:
                            return win
                        elif set_ourHand[-2] < set_ophand[-2]:
                            return loss
                        else:
                            return tie

                pass
            ##two_pair
            elif ourRank[0] == 2:

                for i in range(3)[:1]:

                    if ourRank[i] > opponentRank[i]:
                        return win
                    elif ourRank[i] < opponentRank[i]:
                        return loss
                    else:
                        continue
                    set_ourHand.remove(ourRank[i])
                    set_ophand.remove(opponentRank[i])

                #si les 2 cartes de la paire sont dans la main
                for i in range(3):
                    if set_ourHand[i] > set_ophand[i]:
                        return win
                    elif set_ourHand[i] < set_ophand[i]:
                        return loss
                    else:
                        continue
                return tie
            ##pair
            elif ourRank[0] == 1:
                if ourRank[1] > opponentRank[1]:
                    return win
                elif ourRank[1] < opponentRank[1]:
                    return loss
                else:

                    set_ourHand.remove(ourRank[1])
                    set_ophand.remove(opponentRank[1])
                    len = len(set_ourHand)
                    for i in range(len):
                        if set_ourHand[len-i] > set_ophand[len-i]:
                            return win
                        elif set_ourHand[len-i] < set_ophand[len-i]:
                            return loss
                        else:
                            continue
                    return tie
            ##high card
            elif ourRank[0] == 0:
                len = len(ourHand)-1
                for i in range(len):
                    if ourHand_c[len-i] > opHand_c[len-i]:
                        return win
                    elif ourHand_c[len-i] < opHand_c[len-i]:
                        return loss
                    else:
                        continue
                    return tie
        return None

    def HandStrength(self):
        # ahead = tied = behind = 0
        # ourrank = Rank(ourcards, boardcards)
        pass



    def calculate(self):
        """calcul de 1000 probabilités en fonction du nombre d'adversaires
        , des cartes dans les mains du joueur et dans les mains des adversaires"""

        for card in self.played:
            self.possible.remove(card)


        poss1 = self.possible
        poss2 = self.possible
        # TODO: deux possibilités qu'on enlevera la carte calculée à chaque
        #fois pour parcourir toutes les possibilités en évitant le double dipping

        return None

    def convert_to_value(self, hand):
        liste_drole = []
        for carte in hand:
            liste_drole.append(self.hand_to_value[carte])
        return sorted(liste_drole)
        # return sorted([self.hand_to_value[carte] for carte in hand])

    ###FOR TEST PURPOSES
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
    def test_compare(self, ourhand, ophand):
        print("This is our hand: " + str(ourhand))
        print("This is not our hand (opponent): " + str(ophand))
        print("Output of the round is: " + self.compare(ourhand, ophand))

    def create_random_hand(self):
        temp_hand = copy.copy(self.deck)
        ret_hand = []
        while len(ret_hand) < 2:
            if r.choice(self.deck) not in self.test_board:
                ret_hand.append(r.choice(temp_hand))
            else:
                continue
        ret_hand.append(self.test_board)
        return ret_hand

    ###FOR TEST PURPOSES
    def create_random_board(self):
        temp_hand = copy.copy(self.deck)
        ret_hand = []
        possible_length = [3, 4, 5]
        for i in range(r.choice(possible_length)):
            choice = r.choice(temp_hand)
            ret_hand.append(choice)
            temp_hand.remove(choice)
        self.test_board = ret_hand




    #placé les fonctions dans l'ordre en fonction de leur force
    ###PAS ENCORE TESTÉ CELLE LA
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

    def str_flush(self, hand):
        str8 = self.straight(hand)
        try:
            if str8[0] and self.flush(hand)[0]:
                return (True, self.hand_to_value[str8[1]])
        except TypeError:
            return False
        return False


    def four_of_k(self, hand):
        counter = 1
        current = " "
        for i in sorted(hand):
            if current != i[0]:
                current = i[0]
                counter = 1
            elif current == i[0]:
                counter += 1
            if counter >= 4:
                return (True, self.hand_to_value[current])
        return False

    #returns (True, three_of_k, pair)
    ###PAS ENCORE TESTÉ CETTE FONCTION LA
    def full_house(self, hand):
        temp_hand = copy.copy(hand)
        three = self.three_of_k(hand)
        try:
            if three[0]:
                for carte in hand:
                    if carte[0] == three[1]:
                        temp_hand.remove(carte)
                pair = self.pair(temp_hand)
                if pair[0]:
                    return(True, self.hand_to_value[three[1]], self.hand_to_value[pair[1]])
        except TypeError:
            return False


    ###PAS ENCORE TESTÉ CETTE FONCTION LA
    def flush(self, hand):
        counterh = 0
        currenth = 0
        counterc = 0
        currentc = 0
        counters = 0
        currents = 0
        counterd = 0
        currentd = 0
        for i in hand:
            if i[1] == 'h':
                counterh += 1
                if self.hand_to_value[i] > currenth:
                    currenth = self.hand_to_value[i]
            if i[1] == 'c':
                counterc += 1
                if self.hand_to_value[i] > currentc:
                    currentc = self.hand_to_value[i]
            if i[1] == 's':
                counters += 1
                if self.hand_to_value[i] > currents:
                    currents = self.hand_to_value[i]
            if i[1] == 'd':
                counterd += 1
                if self.hand_to_value[i] > currentd:
                    currentd = self.hand_to_value[i]
        if counterd >= 5:
            return (True, currentd)
        elif counters >= 5:
            return (True,currents)
        elif counterc >= 5:
            return (True,currentc)
        elif counterh >= 5:
            return (True,currenth)
        return False

    def straight(self, hand):
        suite = 0
        cartes_valeurs = self.convert_to_value(hand)
        str8 = []
        scartes = set(cartes_valeurs)


        #Pour le cas unique A 2 3 4 5 (6) (7)
        if scartes.intersection({14, 2, 3, 4, 5, 6, 7}) == {14, 2, 3, 4, 5, 6, 7}:
            return(True, "7")
        elif scartes.intersection({14, 2, 3, 4, 5, 6}) == {14, 2, 3, 4, 5, 6}:
            return(True, "6")
        elif scartes.intersection({14, 2, 3, 4, 5}) == {14, 2, 3, 4, 5}:
            return(True, "5")

        for i in range(len(cartes_valeurs))[1:]:
            if cartes_valeurs[i] - cartes_valeurs[i-1] == 1:
                if str8 == []:
                    str8.append(cartes_valeurs[i-1])
                str8.append(cartes_valeurs[i])
                suite += 1
            else:
                str8 = []
                suite = 0
        if suite >= 4:
            return (True, str8[-1])
        return False

    def three_of_k(self, hand):
        counter = 1
        current = " "
        for i in sorted(hand):
            if current != i[0]:
                current = i[0]
                counter = 1
            elif current == i[0]:
                counter += 1
            if counter >= 3:
                return (True, self.hand_to_value[current])
        return False

    ###PAS TESTÉ CETTE FONCTION LA ENCORE
    def two_pair(self, hand):
        temp_hand = copy.copy(hand)
        p1 = self.pair(hand)
        try:
            if p1[0]:
                for i in hand:
                    if i[0] == p1[1]:
                        temp_hand.remove(i)
            print(p1)
            p2 = self.pair(temp_hand)
            print(p2)
            if p2[0]:
                return (True, self.hand_to_value[p1[1]], self.hand_to_value[p2[1]])
        except TypeError:
            return False

    def pair(self, hand):
        ### à checker, doit retourner la carte de la paire, et non la carte la plus haute autre que la paire
        current = " "
        vpair = 0
        for i in hand:
            if current != i[0]:
                current = i[0]
            elif current == i[0]:
                if self.hand_to_value[i] > vpair:
                    vpair = self.hand_to_value[i]
        if vpair != 0:
            # return (True, self.value_to_hand[vpair])
            return (True, vpair)
        return False

    def high_card(self, hand):
        if self.hand_to_value[hand[0]] > self.hand_to_value[hand[1]]:
            return (True, self.hand_to_value[hand[0]])
        else:
            return (True, self.hand_to_value[hand[1]])

        # TODO: calcul de probabilités
