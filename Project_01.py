"""
Create a program that asks the user 
to enter their name and their age. 
Print out a message addressed to them 
that tells them the year that they will 
turn 100 years old.
Add on to the previous program by asking 
the user for another number and printing 
out that many copies of the previous message.
Print out that many copies of the previous 
message on separate lines.
"""

import time
year = int((time.strftime("%Y")))
print "Current year is %r." % year
user_name = raw_input("What is your name?\n> ")
user_age = int(raw_input("How old are you?\n> "))
message = "%s, you'll be 100 in the year %d.\n" % (user_name, (100 - user_age + year))
repeat_message_amount = int(raw_input("Now, pick a number between 1 and 50.\n> "))
print message * repeat_message_amount