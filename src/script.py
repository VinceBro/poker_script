import json, requests, pickle, datetime


response = unirest.get("https://poker-odds.p.mashape.com/hold-em/odds?community=5d%2C7c%2CAh&hand=As%2CKd&players=3",
  headers={
    "X-Mashape-Key": "xJIMHRTV3kmshCWoU9PYBhFO8Edfp1DOQoBjsn00juCk8aKN4V",
    "Accept": "application/json"
  }
)



class odds():
    def __init__(self):
        self.counter = 0
        self.apikey = "TODO : insert api-key (subscribe)"
        self.url = "TODO : determine url"
        self.username = " "
        self.NAME = " "
        self.hand = " "
        self.community = " "
        self.odds = 0
        self.continue = "y"
        self.day =

    def initialize(self):
        self.day = datetime.date.today()
        return None


    def store(self):
        return None
    def request(self):
        if self.counter >= 95:
            print("Daily request limit reached try again tomorrow")
            return None
        #TODO call requests

    def count(self):
        self.counter += 1
        if self.counter = 95:

    def main(self):
        self.hand = input("Enter your starting hand: ")
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
                continue



                #TODO call api for results
                print("The odds of winning this hand are: " + self.odds)
