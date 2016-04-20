'''
Generate a random number between 1 and 9
Ask user to guess number between 1 and 9
Tell user whether low, high or correct
Extra
Keep the game going until user types exit
Keep track of how many guesses and print this out at end of game
'''

import random

num = random.randint(1,9)
guess_amt = 0
guess_correct_amt = 0
guess = raw_input("\nGuess a number between 1 and 9.\n"
	"To end game type 'EXIT'\n> ")
	
def start():
	global guess
	if guess == "EXIT" or guess == "Exit" or guess == "exit":
		print "\nYou have guessed %d times and were correct %d times." % (guess_amt,guess_correct_amt)
		print "I'm glad we did this together.\n"
		"It was some real quallity time :)"
		quit()
	else:
		guess_check()

def guess_check():
	global guess
	try:
		guess = int(guess)
		num_comp()
	except ValueError:
		print "\nThat's not a number."
		guess_again()

def num_comp():
	global guess_amt, guess_correct_amt
	if guess < 1 or guess > 9:
		print "\nYour guess of %d is not within range." % guess
		guess_again()
	elif num == guess:
		print "\nWow, You got it correct. Good Job!"
		guess_amt += 1
		guess_correct_amt +=1
		start_over()
	elif num < guess:
		print "\nThat's a little high."
		guess_amt +=1
		guess_again()
	elif num > guess:
		print "\nThat's a little low."
		guess_amt += 1
		guess_again()
	else:
		print "\nI'm sorry, I didn't understand that."
		guess_again()
		
def start_over():
	global guess, num
	guess = raw_input("\nEnter a 1 and 9 to play some more.\n"
	"---OR---\n"
	"To end game type 'EXIT'\n> ")
	num = random.randint(1,9)
	start()

def guess_again():
	global guess
	guess = raw_input("\nGuess again.\n"
	"To end game type 'EXIT'\n> ")
	start()

start()