from script import *
import random as r



class odds(cards, manager):
    def __init__(self):
        super().__init__


        #TODO prends self.deck dans cards et enleve les cartes dans les mains
        #du joueur et les cartes dans community
        self.ophand = []

    def calculate(self, self.hand, self.community, self.deck):
        """calcul de 1000 probabilités en fonction du nombre d'adversaires
        , des cartes dans les mains du joueur et dans les mains des adversaires"""
        ## TODO:  cest pas bon ca faut enlever les cartes sur le jeu
        self.ophand = r.choice(self.deck)


        # TODO: calcul de probabilités
