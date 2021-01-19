# Import and test 3 of the functions from your functions exercise file.

#. Import each function in a different way:
#. 
#. import the module and refer to the function with the . syntax
#. use from to import the function directly
#. use from and give the function a different name

import time 
import math as m
from time import sleep as hold_up

time.sleep(1)
print('All Done!')

print(m.sqrt(4))

print("Wait 5 seconds!")
hold_up(5)
print("OK, you may go now!")

# For the following exercises: 
# read about and use the itertools module from the standard library to help you solve the problem.
import itertools as it
from itertools import combinations 

# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

def combining_lists(list1, list2):
    combo = list1 + list2
    count = 0
    for i in it.combinations(combo, 2):
        print(i)
        count += 1
    return count

combining_lists(letters, numbers)

    
# 2. How many different ways can you combine two of the letters from "abcd"?

import itertools as it
from itertools import combinations_with_replacement

letters2 = ["a", "b", "c", "d"]

def number_of_possibilities(list):
    count = 0
    for i in it.combinations_with_replacement(list, 2):
        print(i)
        count += 1
    return count

number_of_possibilities(letters2)

# Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, it will produce a list of dictionaries.
# Using this data, write some code that calculates and outputs the following information:

import json


with open('profiles.json') as profiles:
    profiles = json.load(profiles)

# Total number of users

print(len(profiles))

# Number of active users

len([profile for profile in profiles if profile['isActive']])

# Number of inactive users

len([profile for profile in profiles if not profile['isActive']])


def handle_commas(num_string):
    return float(num_string.replace(",","").replace("$",""))


# Grand total of balances for all users 

balance_list = [handle_commas(d['balance']) for d in profiles]

sum(balance_list)

# Average balance per user

round((sum(balance_list) / len(profiles)), 2)

# User with the lowest balance

min(balance_list)

# User with the highest balance

max(balance_list)

# Most common favorite fruit
# Least most common favorite fruit

import itertools as it
from collections import Counter

favoriteFruit_list = [d['favoriteFruit'] for d in profiles]

Counter(favoriteFruit_list)


def normalize_name(string):
    # makes string lowercase, removes white space to left and right, and replaces spaces with underscores.
    string = string.lower()
    string = string.strip()  
    # This conditional statement removes all characters from the string eccept what is "not in"
    if not string:
        return string
    elif string[0] not in '1234567890':
        return normalize_name(string[1:])
    return string[0] + normalize_name(string[1:])
        

# Total number of unread messages for all users

greeting_list = [int(normalize_name(d['greeting'])) for d in profiles]

total_number_of_unread_messages = (sum(greeting_list))

total_number_of_unread_messages