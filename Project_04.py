"""
Create a program that asks the user for a number 
and then prints out a list of all the divisors of that number. 
"""

num = raw_input("Pick a number.\n> ")

def isInt(x):
	try:
		int(x)
	except ValueError:
		print "How about you enter a valid number next time."
		quit()

isInt(num)

num = int(num)
divisors = []

try:
	testNum = range(2, num)
except MemoryError:
	print "Number too big."
	quit()

for x in testNum:
	if num % x == 0:
		x = x
		divisors.append(x)	

print "Numbers you can use divisors for %d are: " % num
print divisors