
from algorithm import *


class Manager(Odds):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.odds =Odds() 
        self.wins = 0
        self.continuer = " "

    def print_state(self):
        print("Your hand for this turn is : " + str(self.hand))
        print("The community cards for this turn are now " + str(self.community))
        print("Your odds of winning this turn are : " + str(self.odds.calculate(self.hand, self.community)))




    def flop_boucle(self):
        while True:
            question = input(str("Enter your 1st card (Ex: Kh as for king of hearts, Td as for ten of diamonds)\n"))
            if self.check_card_in_deck(question) is False:
                print("Enter a valid card to continue")
                continue
            else:
                self.hand.append(question)
                break
        while True:
            question = input(str("Enter your 2nd card (Ex: Kh as for king of hearts, Td as for ten of diamonds)\n"))
            if self.check_card_in_deck(question) is False:
                print("Enter a valid card to continue")
                continue
            else:
                self.hand.append(question)
                break
        #### maths pour calculer les odds ######
        print("Your initial odds of winning this hand (pre-flop) are: " + "not calculated yet (faut implémenter pre-flop :(")
        while True:
            self.continuer = input("Do you wish to continue (y or n)?")
            if (self.continuer).lower() == "y":
                i = 1
                while i < 4:

                    self.continuer = input("Enter the first 3 community cards (" + str(i) + "/3) -- enter n to stop: ")
                    if self.check_card_in_deck(self.continuer) is False:
                        print("Enter a valid card to continue")
                        continue
                    elif self.continuer.lower() == "n":
                        self.main_menu()
                    else:
                        (self.community).append(self.continuer)
                        i+=1
                break
            elif self.continuer.lower() == "n":
                self.main_menu()
                break
            else:
                continue
                # while(i < 4):
                #     self.continuer = input("Enter the first 3 community cards (" + str(i) + "/3) -- enter n to stop: ")
                #     if self.check_card_in_deck(self.continuer) is False:
                #         print("Enter a valid card to continue")
                #         continue
                #     elif self.continuer.lower() == "n":
                #         self.main_menu()
                #     else:
                #         self.community.append(self.continuer)
                #         i+=1
        self.print_state()

        while True:
            self.continuer = input("would you like to continue to the next turn? (y/n)")
            if self.continuer.lower() == "y":
                self.turn_boucle()
            elif self.continuer.lower() == "n":
                self.main_menu()
            else:
                continue
    ## TODO: strip si jamais le chum entre des espaces!!!!!!!!!
    ## TODO ajout des 52 cartes pour vérifier l'input du user
    def turn_boucle(self):
        while True:
            self.continuer = input(str("Enter 4th community card \n"))
            if self.check_card_in_deck(self.continuer) is False:
                print("Enter a valid card to continue")
                continue
            (self.community).append(self.continuer)
            break
        self.print_state()

        while True:
            self.continuer = input("would you like to continue to the next turn? (y/n)")
            if self.continuer.lower() == "y":
                self.river_boucle()
            elif self.continuer.lower() == "n":
                self.main_menu()
            else:
                continue

    def river_boucle(self):
        ### marche pas.....
        while True:
            self.continuer = input(str("Enter 5th community card \n"))
            if self.check_card_in_deck(self.continuer) is False:
                print("mauvaise carte mon ami")
                continue
            else:
                (self.community).append(self.continuer)
                break
        self.print_state()
        self.main_menu()
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
            choice = input("What would you like to do? (p: Resume playing, s: View stats, n: Stop playing, t: Test functions (developper))")

            if choice.lower() == "p":
                self.hand = []
                self.community = []
                self.main()
                continue
            elif choice.lower() == "s":
                self.stats()
                continue
            elif choice.lower() == "n":
                sys.exit("Program terminated")
            elif choice.lower() == "t":
                self.test_mode()
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
        self.flop_boucle()
        #TODO call api for result
        print("Your now updated odds of winning this hand are: " + str(self.odds))
        odds.turn_boucle()
        print("Your now updated odds of winning this hand are: " + str(self.odds))
        odds.river_boucle()
        print("The odds of winning this hand are: " + str(self.odds))


    def test_mode(self):
        while True:
            self.continuer = input("What do you wish to test? (f: function, C: calculate, c: compare, n: return to main menu)")
            if self.continuer.lower() == "f":
                print("va falloir faire une fct test function dans odds")
            elif self.continuer == "c":
                self.test_compare()
            elif self.continuer == "C":
                self.test_calculate()
            elif self.continuer.lower() == "n":
                self.main_menu()
            else:
                continue

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
