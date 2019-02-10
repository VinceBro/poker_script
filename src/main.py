import pickle
from script import odds

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
        valide = True
        apikey = input("Enter valid API key: ")
        #TODO :: test pour la validité du api key

        if valide:


if __name__ == "__main__":
    x = [1, 2, 3]
    y = [2, 3 ,4]

    with open("/pickle/x.pickle", "wb") as fich:
        fich.write(pickle.dumps(x))
    with open("/pickle/y.pickle", "wb") as fich:
        fich.write(pickle.dumps(y))
