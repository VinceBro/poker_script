import json,requests, pickle, datetime, sys
#from script import *

def initialize():
    username = ' '
    username = input("Enter username: ")
    odds = {}
    try:
        with open(username + '.pickle', "rb") as fich:
            odds = pickle.loads(fich.read())
        print("Welcome back " + username + " !")
    except FileNotFoundError or KeyError:
        print("No such username was found")
        apikey = ' '
        valide = False
        apikey = input("Enter valid API key: ")


if __name__ == "__main__":
    # odds = odds()
    response = {}
    URL = "https://sf-api-on-demand-poker-odds-v1.p.mashape.com/flop?board=As%2C2h%2CTh&hole=Ac%2C3c"
    headers={
      "X-Mashape-Key": "CwTYMXYWmRmshP8DG1HkXmRgYqySp1298F2jsnVzKB3GGN0cKM",
      "Accept": "application/json"
    }
    response = requests.get(url=URL, headers=headers)  # type: object
    print(response)
    response = json.loads(response.text)
    print(response)

    # response = unirest.get("https://sf-api-on-demand-poker-odds-v1.p.mashape.com/flop?board=As%2C2h%2CTh&hole=Ac%2C3c",
    #               headers={
    #                 "X-Mashape-Key": "CwTYMXYWmRmshP8DG1HkXmRgYqySp1298F2jsnVzKB3GGN0cKM",
    #                 "Accept": "application/json"
    #               }
    #             )

    with open(response + ".pickle", "wb") as fich:
        fich.write(pickle.dumps(x))
