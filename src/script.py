import json, requests, pickle, datetime, sys, itertools


 # for symbol in symbole:
 #
 #        params = {
 #            'function': FUNCTION,
 #            'symbol': symbol,
 #            'apikey': APIKEY,
 #            'outputsize': size,
 #        }
 #
 #        response = requests.get(url=URL, params=params)  # type: object
 #        response = json.loads(response.text)
 #        tuple1 = (str(DEBUT), response['Time Series (Daily)'][str(DEBUT)][str(variable)])
 #        tuple2 = (str(FIN), response['Time Series (Daily)'][str(FIN)][str(variable)])
 #        print('{}({}, {}, {})'.format(symbol, VAL, str(DEBUT), str(FIN)))
 #        print([tuple1, tuple2])

class cards():
    def __init__(self):
        self.SUITS = 'cdhs'
        self.RANKS = '23456789TJQKA'
        self.deck = list(''.join(card) for card in itertools.product(self.RANKS, self.SUITS))
    def __str__(self):
        return self.deck


class hole():
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2


class odds():
    def __init__(self, username, apikey):
        self.counter = 0
        self.apikey = apikey
        self.headers = {
              "X-Mashape-Key": apikey,
              "Accept": "application/json"
            }
        self.url = " "
        self.username = username
        self.NAME = " "
        self.hand = []
        self.community = []
        self.odds = "\n"+"dovid manque encore de pratique"
        self.continuer = "y"
        self.day = datetime.date.today()
        self.shutdown = ""
        self.response = {}

    def initialize(self):
        if self.day != datetime.date.today():
            self.day = datetime.date.today()
            self.counter = 0
        return None

    def convert_to_url(self, cards):
        return "%2C".join(cards)

    def store(self):
        return None

    # pf == pre-flop,
    def request(self, turn, hole, board = []):
        self.counter += 1
        if self.counter >= 95 and self.day == datetime.date.today():
            self.store()
            sys.exit("Daily limit reached try again tomorrow")

        if turn == "pre-flop":
            self.url = "https://sf-api-on-demand-poker-odds-v1.p.mashape.com/pre-flop?hole=" + convert_to_url(hole)
        else:
            self.url = "https://sf-api-on-demand-poker-odds-v1.p.mashape.com/" + turn + "?board=" + convert_to_url(board) + "&hole=" + convert_to_url(hole)

        self.response = requests.get(url=self.url, headers=self.headers)
        self.response = json.loads(response.text)
        #TODO faut décider ici si on return le response sans l'enregistrer dans la classe ou on return rien et on l'enregistre dans la classe

    def count(self):
        self.counter += 1
        if self.counter == 95:
            pass

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
    odds = odds('remi', "CwTYMXYWmRmshP8DG1HkXmRgYqySp1298F2jsnVzKB3GGN0cKM")
    cards = cards()
    odds.main()
