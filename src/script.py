import json, requests, pickle, datetime, sys, itertools, copy, time
import random as r
from algorithm import Odds
# import importlib
# importlib.import_module(algorithm)

class Manager(object):
    def __init__(self):
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

    def n_shutdown(self, str_decision):
        if (str_decision).lower() == "n":
            sys.exit("--- program terminated ---")
        return None

    def flop_boucle(self):
        while True:
            question = input(str("Enter your 1st card (Ex: Kh as for king of hearts)\n"))
            if self.check_card_in_deck(question) is False:
                print("mauvaise carte mon ami")
                continue
            break
        while True:
            question = input(str("Enter your 2st card (Ex: Kh as for king of hearts)\n"))
            if self.check_card_in_deck(question) is False:
                print("mauvaise carte mon ami")
                continue
            break
        #### maths pour calculer les odds ######
        print("Your initial odds of winning this hand (pre-flop) are: " + str(self.odds))
        while True:
            self.continuer = input("Do you wish to continue (y or n)?")
            self.n_shutdown(self.continuer)
            if (self.continuer).lower() == "y":
                i = 1
                while(i < 4):
                    self.continuer = input("Enter the first 3 community cards (" + str(i) + "/3) -- enter n to stop: ")
                    self.n_shutdown(self.continuer)
                    if self.check_card_in_deck(self.continuer) is False:
                        print("mauvaise carte mon grand ami")
                        continue
                    self.community.append(self.continuer)
                    i+=1

                print("the flop cards for this turn are  " + str(self.community))
                break
            else:
                print("es-tu attardé?")

    ## TODO: strip si jamais le chum entre des espaces!!!!!!!!!
    ## TODO ajout des 52 cartes pour vérifier l'input du user
    def turn_boucle(self):
        while True:
            question = input(str("Enter 4th community card \n"))
            if self.check_card_in_deck(question) is False:
                print("mauvaise carte mon ami")
                continue
            self.community.append(question)
            break

        print("the community cards for this turn are now " + str(self.community))
        self.shutdown = input("would you like to continue to the next turn? (y/n)")
        self.n_shutdown(self.shutdown)

    def river_boucle(self):
        ### marche pas.....
        self.community.append(input("Enter the 5th community card: "))
        while True:
            question = input(str("Enter 5th community card \n"))
            if self.check_card_in_deck(question) is False:
                print("mauvaise carte mon ami")
                continue
            break
        self.shutdown = input("would you like to continue to the next turn? (y/n)")
        self.n_shutdown(self.shutdown)

    def check_hand_in_deck(self, numero_de_carte):
        valeur = str(self.hand[numero_de_carte])
        if valeur not in self.deck:
            print(self.deck)
            print("card {} is not in deck mon chum".format(valeur))
            return False
        else:
            return True

    def check_card_in_deck(self, carte):
        if carte not in self.deck:
            # print(self.deck)
            # print("card {} is not in deck mon chum".format(carte))
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
    def stats(self):
        print("User: " + self.username + "has played" + self.counter + "hands since he started playing on" + self.date)
        print("You have a " + self.counter/self.wins + "winrate with this script")


    def main(self):
        ## flop et preflop
        odds.flop_boucle()
        #TODO call api for result
        print("Your now updated odds of winning this hand are: " + str(self.odds))
        odds.turn_boucle()
        print("Your now updated odds of winning this hand are: " + str(self.odds))
        odds.river_boucle()
        print("The odds of winning this hand are: " + str(self.odds))




if __name__ == '__main__':
    #manager = Manager('romi')
    #cards = Cards()
    #enlever username de odds ca gosse en criss
    odds = Odds('romi')
    # counter = 0
    # odds.played = ['3s', '4d', '5d', '6s','7d']
    # odds.update_deck()
    # # print(odds.create_all_4_cards())
    # print(odds.HandPotential(odds.played))


    # while True:
    #
    #     odds.test_calculate()
    #     # print(odds.cunter)
    #     # odds.test_compare()
    #     input("")

    ## Pour tester compare
    # while True:
    #     if test.
    #     counter += 1
    #     odds.test_board = []
    #     odds.create_random_board()
    #     odds.test_compare()


    # print(odds.compare(['2s', '3d','4d', 'Td', '6d'],['2s', '3d','4d', 'Td', '6d','5s']))

        # print("\n" * 3)
