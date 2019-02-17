from script import *
import random as r



class odds(cards):
    def __init__(self):
        super().__init__()


        #TODO prends self.deck dans cards et enleve les cartes dans les mains
        #du joueur et les cartes dans community
        self.possible = r.choice(self.deck)
        self.played = self.hand + self.community

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


    # TODO: compare est la fonction qui sera appelée 1000000 fois
    #elle doit donc être extrêmement efficace
    def compare(self):
        pass


    #placé les fonctions dans l'ordre en fonction de leur force
    def roy_flush(self, hand):
        #ici self.played peut être facilement remplacé par hand
        valid = True
        type = hand[0][1]
        roy = ['A', 'K', 'Q', 'J', '10']
        for i in range(hand):
            if type != hand[i][1]:
                valid = False
            #ici la méthode considère que self.played ou hand sont en ordre!!
            if roy[i] != hand[i][0]:
                valid = False
        return valid

    def str_flush(self, hand):
        if straight(hand)[0] and flush(hand)[0]:
            return True
        return False
    # cest legit three_of_k
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
    def full_house(self, hand):
        pass
    def flush(self, hand):
        counterh = 0
        counterc = 0
        counters = 0
        counterd = 0
        for i in hand:
            if i[1] == 'h':
                counterh += 1
            if i[1] == 'c':
                counterc += 1
            if i[1] == 's':
                counters += 1
            if i[1] == 'd':
                counterd += 1
            if counterd >= 5 or counterc >= 5 or counters >= 5 or counterd >= 5:
                return True
        return False

    # à refaire avec value_to_hand et hand_to_value
    def straight(hand):
        suite = 0
        valid = False
        cartes_valeurs = []
        str8 = []
        for carte in hand:
            cartes_valeurs.append(self.hand_to_value[carte])
        cartes_valeurs = sorted(cartes_valeurs)
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
    def two_pair(self, hand):
        current = " "
        counter = 0
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
    def high_card(self, hand):
        pass
        # TODO: calcul de probabilités
