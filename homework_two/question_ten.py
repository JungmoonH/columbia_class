from numpy.random import seed
from numpy.random import randint
seed(1000)
listing = randint(0, 10, 10000)
listing = listing.tolist()

listing.sort()
result = listing[0]
