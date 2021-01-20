# 1. 
# 
# Write a function named isnegative. 
# It should accept a number and return a boolean value 
# based on whether the input is negative.

def isnegative(x):
    return x < 0

# 2. 
# Write a function named count_evens. It should accept a list and return the number of even numbers in the list.

def count_evens(num_list):
    count = 0
    for number in num_list:
        if number % 2 == 0:
            count += 1
    return count

# 3. 
# Write a function named increment_odds. 
# It should accept a list of numbers and return a new list 
# with the odd numbers from the original list incremented.

def increment_odds(myList=[]):
    new_list = []
    for number in myList:
        # if number is even return number
        if (number % 2) == 0:
            return new_list.append(number)
        # if number is odd return number + 1
        else:
            return new_list.append(number + 1)

# 4. 

def average(list_of_numbers=[]):
    return float((sum(list_of_numbers) / len(list_of_numbers)))

# 5. 

def name_to_dict(full_name):
    name = [full_name.split(' ')]
    return {'first_name': name[0], 'last_name': name[1]}

# 6. 

def capitalize_name(names):
    for name in names:
        name['first_name'].append = name['first_name'].capitalize()
        name['last_name'].append = name['last_name'].capitalize() 

# 7.

def count_vowels(string):
    count = 0
    string = string.lower()
    for c in string:
        if c in 'aeiou':
            count += 1
        return count

# 8.

