"""
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains 
only the elements that are common between the lists 
(without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:
Randomly generate two lists to test this
"""

import random
print "----------------------------------------"
a = random.sample(range(1, 100),random.randint(1, 50))
print "The first randomized list of numbers is:\n", a
print "----------------------------------------"
a.sort()

b = random.sample(range(1, 100),random.randint(1, 50))
print "The second randomized list of numbers is:\n", b
print "----------------------------------------"
b.sort()

c = []

for x, y in zip(a, a[1:]):
	if x == y:
		a.remove(x)
		
for x, y in zip(b, b[1:]):
	if x == y:
		b.remove(x)
		
for x in a:
	if x in b:
		x = x
		x = x
		c.append(x)

print "The numbers they have in common are:\n", c
