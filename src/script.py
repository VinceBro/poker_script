import json, requests, pickle, datetime, sys


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

class odds():
    def __init__(self, username, apikey):
        self.counter = 0
        self.apikey = apikey
        self.url = "TODO : determine url"
        self.username = username
        self.NAME = " "
        self.hand = " "
        self.community = " "
        self.odds = 80.00
        self.continue = "y"
        self.day = datetime.date.today()

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
    def request(self, turn, board = [], hole):
        self.counter += 1
        if self.counter >= 95 and self.day == datetime.date.today():
            self.store()
            sys.exit("Daily limit reached try again tomorrow")

        if turn == "pre-flop":

            response = unirest.get("https://sf-api-on-demand-poker-odds-v1.p.mashape.com/pre-flop?hole=" + convert_to_url(hole),
              headers={
                "X-Mashape-Key": "CwTYMXYWmRmshP8DG1HkXmRgYqySp1298F2jsnVzKB3GGN0cKM",
                "Accept": "application/json"
              }
            )

        else:
            response = unirest.get("https://sf-api-on-demand-poker-odds-v1.p.mashape.com/" + turn + "?board=" + convert_to_url(board) + "&hole=" + convert_to_url(hole) ,
              headers={
                "X-Mashape-Key": "CwTYMXYWmRmshP8DG1HkXmRgYqySp1298F2jsnVzKB3GGN0cKM",
                "Accept": "application/json"
              }
            )
    def count(self):
        self.counter += 1
        if self.counter = 95:

    def main(self):
        self.hand = input("Enter your starting hand: \n Ex: jh 3d")
        #TODO call api for result
        print("Your initial odds of winning this hand are: " + self.odds)
        self.continue = input("Do you wish to continue (y or n)?")


        while True:
            if (self.continue).lower() == "y":
                for i in range(3):
                    self.community = input("Enter community cards(enter n to stop): ")
            elif self.community == "N" or self.community == "n":
                break
            else:
                print("Do you wish to continue (y or n)?")
                continue



                #TODO call api for results
            print("The odds of winning this hand are: " + self.odds)
