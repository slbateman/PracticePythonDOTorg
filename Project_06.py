'''
Ask the user for a string and print out whether 
this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

word = raw_input("Enter a word or phrase to check if it is a palindrome.\n> ")
word_rvrs = word[::-1]

if word == word_rvrs:
	print "This is a palindrome."
else:
	print "This is not a palindrome"
