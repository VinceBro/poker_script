from algorithm import Odds
import time

start = time.time()
odds = Odds()
odds.HandPotential(['Ah', '2d'], ['5c', '3h', '9d'])
end = time.time()
print (end - start)
