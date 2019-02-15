from script import *
import random as r



class odds(cards, manager):
    def __init__(self):
        super().__init__


        #TODO prends self.deck dans cards et enleve les cartes dans les mains
        #du joueur et les cartes dans community
        self.possible = r.choice(self.deck)
        self.played = self.hand + self.community

    def calculate(self, self.hand, self.community, self.deck):
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
        #lol
        pass
    def str_flush(self, hand):
        pass
    def four_of_k(self, hand):
        pass
    def full_house(self, hand):
        pass
    def flush(self, hand):
        pass
    def straight(self, hand):
        pass
    def three_of_k(self, hand):
        pass
    def two_pair(self, hand):
        pass

    def pair(self, hand):
        pass
    def high_card(self, hand):
        pass
        # TODO: calcul de probabilités
