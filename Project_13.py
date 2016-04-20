'''
Write a program that asks the user how many 
Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers 
in the sequence to generate
'''
num_num = ""
current_num = 1
previous_num = 0
next_num = 0
fib_nums = []

def get_num():
	global num_num
	try:
		num_num = raw_input("\nHow many Fibonnaci numbers should we generate?\n> ")
		num_num = int(num_num)
		create_fib()
	except KeyboardInterrupt:
		quit()
	except ValueError:
		print "Not a valid number."
		get_num()


def create_fib():
	global num_num, current_num, previous_num, next_num, fib_nums
	for x in range(0, num_num):
		fib_nums.append(current_num)
		next_num = current_num + previous_num
		previous_num = current_num
		current_num = next_num
		
def reset_num():
	global num_num, current_num, previous_num, next_num, fib_nums
	num_num = ""
	current_num = 1
	previous_num = 0
	next_num = 0
	fib_nums = []

while 1==1:
	get_num()
	print "\nYour list of Fibonnaci numbers are: \n%r\n" % fib_nums
	print "Press CRTL-C to quit."
	reset_num()