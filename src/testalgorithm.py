def test_function(self, hand):
    wait = ""
    dict = {"hand" : [], "stats": {"roy_flush": [],"str_flush": [], "four_of_k" : [], "full_house": [], "flush": [], "straight" : [], "three_of_k": [], "two_pair": [], "pair" : [] }}
    functions = [roy_flush(hand), str_flush(hand), four_of_k(hand), full_house(hand), flush(hand), straight(hand), three_of_k(hand), two_pair(hand), pair(hand)]
    for function in dict["stats"]:
        for j in functions:
        dict["stats"][i].append(j)
        print("This is the current hand: " + hand)
        print("For function: " + str(function))
        print("Current output is: " + j)
        wait = input("Press enter to continue")

def create_random_hand(self):
    temp_hand = []
    possible_length = [5, 6, 7]
    for i in range(r.choice(possible_length)):
        temp_hand.append(r.choice(self.deck))
    return temp_hand


test_function()
