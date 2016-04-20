'''
Write a password generator in Python. 
Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password 
every time the user asks for a new password. 
Include your run-time code in a main method
Extra
Ask the user how strong they want there passord
'''
import string
import random

print "------------------------------------------"
print "\n----Welcome to the password generator!----"
print "------------------------------------------"

pw_strength = 0
pw_length = 0
password = []

list_letL = list(string.ascii_lowercase)
list_letU = list(string.ascii_uppercase)
list_num = list(string.digits)
list_sym = list(string.punctuation)

char_dict = {1:list_letL, 2:list_letU, 3:list_num, 4:list_sym[0:12]}

def get_strength():
	global pw_strength, password
	reset_var()
	print "\nPress CRT-C to quit\n"
	pw_strength = raw_input("On a scale of 1-3:\nHow strong would you like you password?\n> ")
	get_length()
	
def get_length():
	global pw_length, pw_strength
	while pw_length == 0:
		if pw_strength == "1":
			pw_length = 5
		elif pw_strength == "2":
			pw_length = 8
		elif pw_strength == "3":
			pw_length = 12
		else:
			print "Enter a 1 or 2 or 3, please try it again.\n"
			pw_strength = raw_input("> ")
	set_pw()

def set_pw():
	global pw_strength
	if pw_strength == "1":
		set_weak()
	elif pw_strength == "2":
		set_med()
	elif pw_strength == "3":
		set_strong()
	else:
		print "An error occurred. Let's try again."
		get_strength()
	
def set_weak():
	global pw_length, password
	for x in range(0, pw_length):
		x = get_char()
		password.append(x)
	password = ''.join(password)

def set_med():
	global pw_length, password
	for x in range(0, pw_length):
		x = get_char()
		password.append(x)
	password = ''.join(password)

def set_strong():
	global pw_length, password
	for x in range(0, pw_length):
		x = get_char()
		password.append(x)
	password = ''.join(password)

def get_char():
	global char_dict, pw_strength
	if pw_strength == "1":
		x = char_dict[random.randint(1,2)]
	elif pw_strength == "2":
		x = char_dict[random.randint(1,3)]
	elif pw_strength == "3":
		x = char_dict[random.randint(1,4)]
	else:
		print "An error occurred. Let's try again."
		get_strength()
	y = random.randint(0,len(x) - 1)
	z = x[y]
	return z
	
def reset_var():
	global pw_length, password
	pw_length = 0
	password = []

while 1 == 1:
	get_strength()
	print "\n---> Your password is:"
	print "--->    ", password	