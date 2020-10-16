from numpy.random import seed
from numpy.random import randint
seed(1000)
listing = randint(1, 10, 10000)
listing = listing.tolist()

result = []
for value in listing:
    if value not in result:
        result.append(value)
            
