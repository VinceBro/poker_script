from script import *
import random as r



class odds(cards, manager):
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
        valide = True
        type = hand[0][1]
        str = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']


    def four_of_k(self, hand):
        pass
    def full_house(self, hand):
        pass
    def flush(self, hand):
        valid = True
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
            valid = True
        return valid


    def straight(self):
        check1 = 0
        suite = 0
        cartes = manager.hand + manager.community
        for carte in sorted(cartes):
            if self.value[carte]
    def three_of_k(self, hand):
        pass
    def two_pair(self, hand):
        pass

    def pair(self, hand):
        pass
    def high_card(self, hand):
        pass
        # TODO: calcul de probabilités
