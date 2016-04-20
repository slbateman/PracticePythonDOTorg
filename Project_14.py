'''
Write a program (function!) that takes a list 
and returns a new list that contains all the 
elements of the first list minus all the duplicates
'''

import random
list = []
list_new = []

for x in range(1, random.randint(10, 20)):
	list.append(random.randint(1, 9))

def remove_dup(x, y):
	for n in x:
		if n not in y:
			y.append(n)

print list
remove_dup(list, list_new)
print list_new
