import itertools
import random

class MovesIterator:

    def __init__(self):
        self.moves = ("N", "E", "S", "W")
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return random.choice(self.moves)
        
        
it1 = itertools.cycle(range(2))
it2 = MovesIterator()
it3 = itertools.cycle(range(7))


for i in range(25):
    print(next(it1), end=' ')
    
print('')

for i in range(25):
    print(next(it2), end=' ')
    
print('')
    
for i in range(25):
    print(next(it3), end=' ')
    
print('')
    
