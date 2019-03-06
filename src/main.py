import json, pickle, datetime, sys, time
from script import *

def initialize():
    if True:
        print("""

   ___       __                        _      __
  / _ \___  / /_____ ____ ___ ________(_)__  / /_
 / ___/ _ \/  '_/ -_) __/(_-</ __/ __/ / _ \/ __/
/_/   \___/_/\_\\__ /_/__/___/\__/_/ /_/ .__/\__/
                    /___/            /_/

""")
        print("v0.0.5(beta)")
        print("Made by: jack_sparrow and davy_jones")
        time.sleep(3)
    manager = {}
    try:
        with open('poker_script.pickle', "rb") as fich:
            manager = pickle.loads(fich.read())
        return manager

    except FileNotFoundError or KeyError:
        return manager

        # while True:
        #
        #     apikey = input("Please enter a valid API key: ")
        #     headers={
        #       "X-Mashape-Key": apikey,
        #       "Accept": "application/json"
        #     }
        #
        #     try:
        #         response = requests.get(url=URL, headers=headers)  # type: object
        #         response = json.loads(response.text)
        #         response['message']
        #         continue
        #
        #     except KeyError:
        #         print("Valid API key")
        #         time.sleep(.500)
        #         print("New user created: " + username)
        #         time.sleep(.500)
        #         manager = manager(username, apikey)
        #         manager.initialize()
        #         return manager


if __name__ == "__main__":
    try:
        manager = initialize()
    except:
        print("Ending Session, Saving...")
        with open("poker_script.pickle", "wb") as fich:
            fich.write(pickle.dumps(manager))


    # response = unirest.get("https://sf-api-on-demand-poker-odds-v1.p.mashape.com/flop?board=As%2C2h%2CTh&hole=Ac%2C3c",
    #               headers={
    #                 "X-Mashape-Key": "CwTYMXYWmRmshP8DG1HkXmRgYqySp1298F2jsnVzKB3GGN0cKM",
    #                 "Accept": "application/json"
    #               }
    #             )
    #
    # with open("response.pickle", "wb") as fich:
    #     fich.write(pickle.dumps(response))
