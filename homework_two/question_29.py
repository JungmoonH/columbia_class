from numpy.random import seed
from numpy.random import randint
seed(1000)
listing = randint(1, 10, 10000)
listing = listing.tolist()

value_ratios = {}
for value in listing:
    value_ratios[value] = listing.count(value)/10000
    
    
