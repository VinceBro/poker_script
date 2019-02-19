<<<<<<< HEAD
from script import *
import random as r



class odds(cards):
    def __init__(self):
        super().__init__()


        #TODO prends self.deck dans cards et enleve les cartes dans les mains
        #du joueur et les cartes dans community
        self.possible = r.choice(self.deck)
        self.played = self.hand + self.community
        self.testing_dict = {"hand" : [], "stats": {"roy_flush": [],"str_flush": [], "four_of_k" : [], "full_house": [], "flush": [], "straight" : [], "three_of_k": [], "two_pair": [], "pair" : [] }}


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
        cartes_valeurs = []
        for carte in hand:
            cartes_valeurs.append(self.hand_to_value[carte])
        return sorted(cartes_valeurs)
    # TODO: compare est la fonction qui sera appelée 1000000 fois
    #elle doit donc être extrêmement efficace
    def compare(self):
        pass

    ###FOR TEST PURPOSES
    def test_function(self, hand):
        wait = ""
        dict = {"hand" : [], "stats": {"roy_flush": self.roy_flush(hand),"str_flush": self.str_flush(hand), "four_of_k" : self.four_of_k(hand), "full_house": self.full_house(hand), "flush": self.flush(hand), "straight" : self.straight(hand), "three_of_k": self.three_of_k(hand), "two_pair": self.two_pair(hand), "pair" : self.pair(hand) }}
        for function in dict["stats"]:
            dict["stats"][function]
            print("This is the current hand: " + hand)
            print("For function: " + function)
            print("Current output is: " + dict["stats"][function])
            wait = input("Press enter to continue")

    ###FOR TEST PURPOSES
    def create_random_hand(self):
        choice = " "
        temp_hand = self.deck
        ret_hand = []
        possible_length = [5, 6, 7]
        for i in range(r.choice(possible_length)):
            choice = r.choice(self.deck)
            ret_hand.append(choice)
            temp_hand.remove(choice)
        return ret_hand




    #placé les fonctions dans l'ordre en fonction de leur force
    ###PAS ENCORE TESTÉ CELLE LA
    def roy_flush(self, hand):
        temp_hand = hand
        cartes_valeurs = convert_to_value(hand)
        scartes = set(cartes_valeurs)
        if scartes.intersection({14, 13, 12, 11, 10}) == {14, 13, 12, 11, 10}:
            for carte in hand:
                if self.hand_to_value[carte] != 14 or self.hand_to_value[carte]!= 13 or self.hand_to_value[carte] != 12 or self.hand_to_value[carte] != 11 or self.hand_to_value[carte] != 10:
                    temp_hand.remove(carte)
            if flush(temp_hand):
                return True
        return False

    def str_flush(self, hand):
        str8 = straight(hand)
        if str8[0] and flush(hand)[0]:
            return (True, str8[1])
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
                return (True, current)
        return False

    #returns (True, three_of_k, pair)
    ###PAS ENCORE TESTÉ CETTE FONCTION LA
    def full_house(self, hand):
        temp_hand = hand
        three = self.three_of_k(hand)
        if three[0]:
            for carte in hand:
                if carte[0] == three[1]:
                    temp_hand.remove(carte)
            pair = self.pair(temp_hand)
            if pair[0]:
                return(True, three[1], pair[1])
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
            return (True,self.value_to_hand[currentd])
        elif counters >= 5:
            return (True,self.value_to_hand[currents])
        elif counterc >= 5:
            return (True,self.value_to_hand[currentc])
        elif counterh >= 5:
            return (True,self.value_to_hand[currenth])
        return False

    def straight(hand):
        suite = 0
        valid = False
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


        for i in range(len(sorted(cartes_valeurs))):
            print(i)
            if suite >= 3:
                valid = True
            if cartes_valeurs[i] - cartes_valeurs[i-1] == 1:
                str8.append(cartes_valeurs[i])
                suite += 1
            elif str8 != [] and suite < 3:
                str8 = []
            else:
                suite = 0
        if valid:
            return (True, self.value_to_hand[str8[-1]])
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
                return (True, current)
        return False

    ###PAS TESTÉ CETTE FONCTION LA ENCORE
    def two_pair(self, hand):
        temp_hand = hand
        p1 = pair(hand)
        if p1[0]:
            for i in hand
                if i[0] == pair[1]:
                    temp_hand.remove(i)
        p2 = pair(temp_hand)
        if p2[0]:
            return (True, p1[1], p2[1])
        return False

    def pair(self, hand):
        current = " "
        vpair = 0
        for i in sorted(hand):
            if current != i[0]:
                current = i[0]
            elif current == i[0]:
                if self.hand_to_value[i] > vpair:
                    vpair = self.hand_to_value[i]
        if vpair != 0:
            return (True, self.value_to_hand[vpair])
        return False

    #pas nécéssaire
    def high_card(self, hand):
        pass
        # TODO: calcul de probabilités
=======
# from script import *
# import random as r
#
#
# 
# class odds(cards):
#     def __init__(self):
#         super().__init__()
#
#
#         #TODO prends self.deck dans cards et enleve les cartes dans les mains
#         #du joueur et les cartes dans community
#         self.possible = r.choice(self.deck)
#         self.played = self.hand + self.community
#
#     def calculate(self):
#         """calcul de 1000 probabilités en fonction du nombre d'adversaires
#         , des cartes dans les mains du joueur et dans les mains des adversaires"""
#
#         for card in self.played:
#             self.possible.remove(card)
#
#
#         poss1 = self.possible
#         poss2 = self.possible
#         # TODO: deux possibilités qu'on enlevera la carte calculée à chaque
#         #fois pour parcourir toutes les possibilités en évitant le double dipping
#
#         return None
#
#
#     # TODO: compare est la fonction qui sera appelée 1000000 fois
#     #elle doit donc être extrêmement efficace
#     def compare(self):
#         pass
#
#
#     #placé les fonctions dans l'ordre en fonction de leur force
#     def roy_flush(self, hand):
#         #ici self.played peut être facilement remplacé par hand
#         valid = True
#         type = hand[0][1]
#         roy = ['A', 'K', 'Q', 'J', '10']
#         for i in range(hand):
#             if type != hand[i][1]:
#                 valid = False
#             #ici la méthode considère que self.played ou hand sont en ordre!!
#             if roy[i] != hand[i][0]:
#                 valid = False
#         return valid
#
#     def str_flush(self, hand):
#         if straight(hand)[0] and flush(hand)[0]:
#             return True
#         return False
#     # cest legit three_of_k
#     def four_of_k(self, hand):
#         counter = 1
#         current = " "
#         for i in sorted(hand):
#             if current != i[0]:
#                 current = i[0]
#                 counter = 1
#             elif current == i[0]:
#                 counter += 1
#             if counter >= 4:
#                 return (True, current)
#         return False
#     def full_house(self, hand):
#         pass
#     def flush(self, hand):
#         counterh = 0
#         counterc = 0
#         counters = 0
#         counterd = 0
#         for i in hand:
#             if i[1] == 'h':
#                 counterh += 1
#             if i[1] == 'c':
#                 counterc += 1
#             if i[1] == 's':
#                 counters += 1
#             if i[1] == 'd':
#                 counterd += 1
#             if counterd >= 5 or counterc >= 5 or counters >= 5 or counterd >= 5:
#                 return True
#         return False
#
#     #Y manque le cas A 2 3 4 5
#     def straight(hand):
#         suite = 0
#         valid = False
#         cartes_valeurs = []
#         str8 = []
#         for carte in hand:
#             cartes_valeurs.append(self.hand_to_value[carte])
#         cartes_valeurs = sorted(cartes_valeurs)
#         scartes = set(cartes_valeurs)
#
#
#         # Regarde pour le cas unique A 2 3 4 5 (6) (7)
#         if scartes.intersection({14, 2, 3, 4, 5, 6, 7}) == {14, 2, 3, 4, 5, 6, 7}:
#             return(True, "7")
#         elif scartes.intersection({14, 2, 3, 4, 5, 6}) == {14, 2, 3, 4, 5, 6}:
#             return(True, "6")
#         elif scartes.intersection({14, 2, 3, 4, 5}) == {14, 2, 3, 4, 5}:
#             return(True, "5")
#
#
#         for i in range(len(sorted(cartes_valeurs))):
#             print(i)
#             if suite >= 3:
#                 valid = True
#             if cartes_valeurs[i] - cartes_valeurs[i-1] == 1:
#                 str8.append(cartes_valeurs[i])
#                 suite += 1
#             elif str8 != [] and suite < 3:
#                 str8 = []
#             else:
#                 suite = 0
#         if valid:
#             return (True, self.value_to_hand[str8[-1]])
#         return False
#     def three_of_k(self, hand):
#         counter = 1
#         current = " "
#         for i in sorted(hand):
#             if current != i[0]:
#                 current = i[0]
#                 counter = 1
#             elif current == i[0]:
#                 counter += 1
#             if counter >= 3:
#                 return (True, current)
#         return False
#     def two_pair(self, hand):
#         current = " "
#         counter = 0
#         vpair1 = 0
#         vpair2 = 0
#         for i in sorted(hand):
#             if current != i[0]:
#                 current = i[0]
#             elif current == i[0]:
#                 counter += 1
#                 if self.hand_to_value[i] > vpair:
#                     vpair = self.hand_to_value[i]
#         if counter >= 2:
#             return (True, self.value_to_hand[vpair1], self.value_to_hand[vpair2])
#         return False
#
#     def pair(self, hand):
#         current = " "
#         vpair = 0
#         for i in sorted(hand):
#             if current != i[0]:
#                 current = i[0]
#             elif current == i[0]:
#                 if self.hand_to_value[i] > vpair:
#                     vpair = self.hand_to_value[i]
#         if vpair != 0:
#             return (True, self.value_to_hand[vpair])
#         return False
#     def high_card(self, hand):
#         pass
#         # TODO: calcul de probabilités
>>>>>>> d90552c9606124d0536c6035f88f1f7bd47906d7
