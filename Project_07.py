'''
Let's say I give you a list saved in a variable.
Write one line of code that takes this list and
makes a new list that only has the even elements.
'''

import random

a = random.sample(range(1, 100), 10)
b = [x for x in a if x %2 == 0]

print b


