import json, requests, pickle, datetime, sys, itertools
import random as r
# import importlib
# importlib.import_module(algorithm)
from testalgorithm import *

class Cards(object):
    def __init__(self):
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

class Manager(Cards):
    def __init__(self, username):
        super(Manager, self).__init__()
        self.counter = 0
        self.url = " "
        self.username = username
        self.NAME = " "
        self.hand = []
        self.community = []
        self.odds = "\n"+"dovid manque encore de pratique"
        self.continuer = "y"
        self.date = datetime.date.today()
        self.shutdown = ""
        self.wins = 0

    def initialize(self):
        pass

    def store(self):
        return None

    # pf == pre-flop,
        #TODO faut décider ici si on return le response sans l'enregistrer dans la classe ou on return rien et on l'enregistre dans la classe

    def n_shutdown(self, str_decision):
        if (str_decision).lower() == "n":
            sys.exit("--- program terminated ---")
        return None

    def flop_boucle(self):
        while True:
            self.hand.append(input(str("Enter your 1st card (Ex: Kh as for king of hearts)\n")))
            if self.check_hand_in_deck(0) is False:
                continue
            break
        while True:
            self.hand.append(input(str("Enter your 2nd card (Ex: Kh as for king of hearts)\n")))
            if self.check_hand_in_deck(1) is False:
                continue
            break
        #### maths pour calculer les odds ######
        print("Your initial odds of winning this hand (pre-flop) are: " + str(self.odds))
        while True:
            self.continuer = input("Do you wish to continue (y or n)?")
            self.n_shutdown(self.continuer)
            if (self.continuer).lower() == "y":
                for i in range(3):
                    self.continuer = input("Enter the first 3 community cards (" + str(i+ 1) + "/3) -- enter n to stop: ")
                    self.check_in_deck(i+2)
                    self.n_shutdown(self.continuer)
                    self.community.append(self.continuer)

                print("the flop cards for this turn are  " + str(self.community))
                break

    ## TODO: strip si jamais le chum entre des espaces!!!!!!!!!
    ## TODO ajout des 52 cartes pour vérifier l'input du user
    def turn_boucle(self):
        self.shutdown = input("would you like to continue? (y/n)")
        while True:
            self.community.append(input("Enter the 4th community card: "))
            if self.check_community_in_deck(0) is False:
                continue
            break

        print("the community cards for this turn are now " + str(self.community))
        self.shutdown = input("would you like to continue to the next turn? (y/n)")
        self.n_shutdown(self.shutdown)

    def river_boucle(self):
        self.community.append(input("Enter the 5th community card: "))
        print("the community cards for this turn are now " + str(self.community))
        self.shutdown = input("would you like to continue to the next turn? (y/n)")
        self.n_shutdown(self.shutdown)

    def check_hand_in_deck(self, numero_de_carte):
        valeur = str(self.hand[numero_de_carte])
        if valeur not in cards.deck:
            print(cards.deck)
            print("card {} is not in deck mon chum".format(valeur))
            return False
        else:
            return True

#### faire poper si jamais mauvais input, sinon ca continue à loop
    def check_community_in_deck(self, numero_de_carte):
        valeur = str(self.community[numero_de_carte])
        if valeur not in cards.deck:
            print(cards.deck)
            print("card {} is not in deck mon chum".format(valeur))
            return False
        else:
            return True
    def main_menu(self):
        choice = ""
        while True:
            choice = input("What would you like to do? (p: Resume playing, s: View stats, n: Stop playing)")
            self.n_shutdown(choice)

            if choice.lower() == "p":
                main()
                continue
            elif choice.lower() == "s":
                stats()
                continue
            else:
                continue
            choice = input("Did you win this hand? (y/n)")
            if choice.lower() == y:
                print("Adding won hand to stats")
            elif choice.lower() == n:
                print("Adding lost hand to stats")

class Odds(Manager):
    def __init__(self, username):
        super().__init__(username)
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

    #Y manque le cas A 2 3 4 5
    def straight(self, hand):
        suite = 0
        valid = False
        cartes_valeurs = []
        str8 = []
        for carte in hand:
            cartes_valeurs.append(self.hand_to_value[carte])
        cartes_valeurs = sorted(cartes_valeurs)
        scartes = set(cartes_valeurs)


        # Regarde pour le cas unique A 2 3 4 5 (6) (7)
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
    def two_pair(self, hand):
        current = " "
        counter = 0
        vpair1 = 0
        vpair2 = 0
        for i in sorted(hand):
            if current != i[0]:
                current = i[0]
            elif current == i[0]:
                counter += 1
                if self.hand_to_value[i] > vpair:
                    vpair = self.hand_to_value[i]
        if counter >= 2:
            return (True, self.value_to_hand[vpair1], self.value_to_hand[vpair2])
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

def main(self):
    ## flop et preflop
    odds.flop_boucle()
    #TODO call api for result
    print("Your now updated odds of winning this hand are: " + str(self.odds))
    odds.turn_boucle()
    print("Your now updated odds of winning this hand are: " + str(self.odds))
    odds.river_boucle()
    print("The odds of winning this hand are: " + str(self.odds))
def stats(self):
    print("User: " + self.username + "has played" + self.counter + "hands since he started playing on" + self.date)
    print("You have a " + self.counter/self.wins + "winrate with this script")


if __name__ == '__main__':
    manager = Manager('romi')
    cards = Cards()
    odds = Odds('romi')
    print(odds.deck)
    print(odds.hand)
    print(odds.straight(['2s','3s','4s','5s','6s']))
    print(odds.pair(['2s','3s','4s','6s','6s']))
