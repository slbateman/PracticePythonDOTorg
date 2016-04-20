"""
Create a program that asks the user for a number 
and then prints out if its a prime number. 
Extra
Use functions
"""

num_rng = []
divisors = []

def get_num():
	num = raw_input("Pick a number.\n> ")
	isInt(num)

def isInt(x):
	global num
	try:
		x = int(x)
		num_test(x)
	except ValueError:
		print "How about you enter a valid number next time."
		get_num()

def num_test(x):
	try:
		num_rng = range(2, x / 2 + 1)
		find_div(x, num_rng)
	except MemoryError:
		print "Number too big."
		get_num()
	except OverflowError:
		print "Number too big."
		get_num()

def find_div(a, b):
	for x in b:
		if a % x == 0:
			a = a
			divisors.append(x)
	print_end(a, divisors)

def print_end(x, y):
	if not y:
		print "%d is a prime number." % x
		start_again()
	else:
		print "%d is not a prime number." % x
		start_again()

def start_again():
	start = raw_input("Would you like to pick a new number? Y/N?\n> ")
	if (start == "Y" or start == "y" or start == "yes" or
	start == "YES" or start == "Yes"):
		get_num()
	else:
		quit()

get_num()