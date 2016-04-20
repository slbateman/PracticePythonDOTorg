"""
Ask the user for a number. 
Depending on whether the number is even or odd 
print out an appropriate message to the user. 
If the number is a multiple of 4, print out a different message
"""

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
	num_quarter = num % 4
	num_half = num % 2
	if num_quarter == 0:
		print "That number is even and divisible by 4."
	elif num_half == 0:
		print "That number is even."
	else:
		print "That number is odd."