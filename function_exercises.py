# Define a function named is_two. It should accept one input and 
# return True if the passed input is either the number 
# or the string 2, False otherwise.

def is_two(x):
    return x == 2 or x == "2"

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(c):
    return c.lower() in 'aeiou'

# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(c):
    return c.isalpha() and not is_vowel(c)
 
        
# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def capitalize_if_consonant(string):
    first_letter = string[0]
    if is_consonant(first_letter):
        return string.capitalize()
    else:
        return string

# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage, bill_total):
    if tip_percentage >= 1 and tip_percentage <= 0:
        print("Tip percentage should be between 0 and 1.")
    else:
        return "{:.2f}".format(tip_percentage * bill_total)

# Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    if discount_percentage >= 1 and discount_percentage <= 0:
        print("Discount percentage should be between 0 and 1.")
    else:
        return (original_price - (original_price * discount_percentage))

# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(num_string):
    return float(num_string.replace(",",""))


# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    else:
        return "F"

# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    string = string.lower()
    if not string:
        return string
    elif string[0] in 'aeiou':
        return remove_vowels(string[1:])
    return string[0] + remove_vowels(string[1:])
    
# Short version
def remove_vowel_small(string):
    return "".join([c for c in string if not is_vowel(c)])


# Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:

#    - anything that is not a valid python identifier should be removed
#    - leading and trailing whitespace should be removed
#    - everything should be lowercase
#    - spaces should be replaced with underscores

def normalize_name(string):
    string = string.lower()
    string = string.rstrip()
    string = string.lstrip()
    string = string.replace(" ","_")
    return string

# Write a function named cumulative_sum 
# that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

def cumulative_sum(lst):
    s = lst.copy()
    for i in range(1, len(s)):
        s[i] += s[i-1]
    return s

# Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm and 
# return a string that is the representation of the 
# time in a 24-hour format. 
# Bonus write a function that does the opposite.

# defines function to accept a string in 12-hour format to convert to 24 hour time
# this is a bit over-kill but it looks nice
def twelveto24(string):
    # converting 1200 am to 0000 hours
    if string[-2:] == "am" and string[:2] == "12":
        return "00" + string[2:-2].replace(":", "") + " hours"
    # checks whether times in the morning contain 4 digits (hh:mm) 
    elif len(string) == 6 and string[-2:] == "am":
        # add 0, removes : and am, and adds hours
        return "0" + string[:-2].replace(":", "") + " hours"
    # times in the morning already containing 4 digits (hh:mm) 
    elif len(string) == 7 and string[-2:] == "am":
        # removes : and am and adds hours
        return string[:-2].replace(":", "") + " hours"
    # converts noon into 24 hour time
    elif string[-2:] == "pm" and string[:2] == "12":
        # the 12 stays the same 
        return string[:-2].replace(":", "") + " hours"
    # checks whether times after noon contain 4 digits (hh:mm) 
    elif len(string) == 6:
        # converts time to hh:mm
        string = "0" + string
        # adds 12 to hh, removes : and pm, adds hours
        return str(int(string[:2]) + 12) + string[2:-2].replace(":", "") + " hours"
    else:
        # returns the rest of the afternoon times ^
        return str(int(string[:2]) + 12) + string[2:-2].replace(":", "") + " hours"
    
