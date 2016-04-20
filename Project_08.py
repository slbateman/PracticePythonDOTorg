'''
Make a two-player Rock-Paper-Scissors game. 
Ask for player plays (using input)
compare them
print out a message of congratulations to the winner, 
and ask if the players want to start a new game

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

import random

user_wins = 0
com_wins = 0
keep_playing = True

def play_again():
	pa = raw_input("Do you want to play again? Y/N ?\n> ")
	if (pa == "Y") or (pa == "yes") or (pa == "Yes") or (pa == "y"):
		keep_playing = True
	else:
		keep_playing = False
		print "\nYou have won %d times and I have won %d times.\n" % (user_wins, com_wins)
		print "Okay, thanks for playing.\n"
		quit()

while keep_playing == True:
	print "\nYou have won %d times and I have won %d times.\n" % (user_wins, com_wins)
	print "Let's play ROCK-PAPER-SCISSORS!"
	
	user_chooses = raw_input("Do you choose: ROCK or PAPER or SCISSORS ?\n> ")
	ran_sel = random.randint(1, 3)
	com_chooses = ()
	


	if ran_sel == 1:
		com_chooses = "ROCK" 
	elif ran_sel == 2:
		com_chooses = "PAPER" 
	else:
		com_chooses = "SCISSORS"
	
	print "\nYou choose '%s' and I choose '%s'.\n" % (user_chooses, com_chooses)
	
	if (user_chooses == "rock" or user_chooses == "paper"
	or user_chooses == "scissors" or user_chooses == "Rock"
	or user_chooses == "Paper" or user_chooses == "Scissors"):
		print "!!!!!!!!!  YOU LOSE  !!!!!!!!!"
		print "Oh, Come on! This is an aggresive game."
		print "You'll always lose unless you use CAPSLOCK!"
		print "!!!!!!!!!  YOU LOSE  !!!!!!!!!\n"
		com_wins += 1
		play_again()
	elif user_chooses == com_chooses:
		print "It's a tie!"
		play_again()
	elif user_chooses == "ROCK" and com_chooses == "SCISSORS":
		print "You WIN! Great Job\n!"
		user_wins += 1
		play_again()
	elif user_chooses == "PAPER" and com_chooses == "ROCK":
		print "You WIN! Great Job!\n"
		user_wins += 1
		play_again()
	elif user_chooses == "SCISSORS" and com_chooses == "PAPER":
		print "You WIN! Great Job!\n"
		user_wins += 1
		play_again()
	else:
		print "Sorry, looks like I WIN.\n"
		com_wins += 1
		play_again()