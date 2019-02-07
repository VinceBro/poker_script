import json, requests, pickle


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
        
    def initialize(self):
        return None
    def store(self):
        