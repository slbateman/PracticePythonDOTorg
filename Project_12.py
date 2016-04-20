'''
Write a program that takes a list of numbers 
a = [5, 10, 15, 20, 25] 
and makes a new list of only the first and last elements
'''
import random

list = random.sample(range(1,100), random.randint(1, 50))
print list

new_list = [list[0], list[-1]]
print new_list