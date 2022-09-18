import random
import itertools
deck = list(itertools.product(range(1, 14), [
            'Hearts', 'Diamond', 'Clubs', 'Spades']))
random.shuffle(deck)
for i in range(52):
    print(deck[i])
