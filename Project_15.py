'''
Write a program that asks the user for a 
long string containing multiple words. 
Print back to the user the same string, 
except with the words in backwards order. 
'''


string = raw_input("\nEnter a long string containing multiple words.\n> ")

def reverse_str(x):
	y = " ".join(x.split(" ")[::-1])
	return y

print reverse_str(string)