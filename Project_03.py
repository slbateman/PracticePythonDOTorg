"""
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the 
elements of the list that are less than 5.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

num = raw_input("Pick a number between 1 and 100.\n> ")

def isInt(x):
	try:
		int(x)
	except ValueError:
		print "How about you enter a number next time."
		quit()

isInt(num)

num = int(num)

if (num < 1 or num > 100):
	print "I said between 1 and 100."
else: 
	for x in a:
		if x < num:
			x = x
			b.append(x)

print b 