# Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is Monday or not
# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

x = input("What's your favorite day of the week? ")

if x.lower() == "Monday":
    print(".... but Monday sucks....")
elif x.lower() == "tuesday" or x.lower() == "wednesday" or x.lower() == "thursday" or x.lower() == "friday":
    print("not a bad weekday choice!") 
elif x.lower() == "saturday" or x.lower() == "sunday":
    print("Duh! It's the weekend!")
else:
    print("That is not a day of the week!")

# c. create variables and make up values for
#     - the number of hours worked in one week
#     - the hourly rate
#     - how much the week's paycheck will be

hours_worked_in_one_week = 60
pay_per_hour = 35
std_work_week = 40
weeks_pay = std_work_week * pay_per_hour

#   write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

if hours_worked_in_one_week <= std_work_week:
    print(weeks_pay)
elif hours_worked_in_one_week > std_work_week:
    overtime_pay = (weeks_pay + ((hours_worked_in_one_week - std_work_week) * (pay_per_hour * 1.5)))

print(overtime_pay)

# 2. Loop Basics

# a. While
#     - Create an integer variable i with a value of 5.
#.    - Create a while loop that runs so long as i is less than or equal to 15
#     - Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i < 15:
    i += 1
    print(i)

# 2. Loop Basics

# a. While
#     - Create an integer variable i with a value of 5.
#.    - Create a while loop that runs so long as i is less than or equal to 15
#     - Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i < 15:
    i += 1
    print(i)

# - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

n = 0 
while n <= 100:
    print(n)
    n += 2

# - Alter your loop to count backwards by 5's from 100 to -10.
n = 100
while n >= -10:
    print(n)
    n -= 5
    
# - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.

n = 2

while n < 1_000_000:
    print(n)
    n = (n ** 2)

# Write a loop that uses print to create the output shown below.
n = 100
while n >= 5: 
    print(n)
    n -= 5

# b. For Loops

#     - Write some code that prompts the user for a number, 
#       then shows a multiplication table up through 10 for that number.

x = int(input("What's your number? "))

for i in range(1,11):
    print(x," x ",i," = ", (x*i))

# Create a for loop that uses print to create the output shown below.

for n in range(1,10):
    print(str(n) * n)

# c. break and continue

# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.

while True:
    user_number = input("Enter an odd number between 1 and 50: ")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number % 2 == 0:
            print("Invalid inpuit: Input is an even number.")
            continue
        elif user_number > 50 or user_number < 0:
            print("Invalid Input: Input is out of range.")
            continue
        break

i = 1
while i <= 50:
    if i == user_number:
        print(f"Yikes! Skipping number: {i}")
        i += 2
        continue
    print(f"Here is an odd number: {i}")
    i += 2
        
#  The input function can be used to prompt for input and use that input in your python code. 
#  Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#  (Hints: first make sure that the value the user entered is a valid number, 
#  also note that the input function returns a string, so you'll need to convert this to a numeric type.)

#  Write a program that prompts the user for a positive integer. 
#  Next write a loop that prints out the numbers from the number the user entered down to 1.

while True:
    user_number = input("Enter a positive number: ")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number <= 0:
            continue
        break

# for i in range(0, user_number + 1):
#     print(i)
    
for i in range(user_number, 0, -1):
    print(i)

# 3. Fizzbuzz

# - One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# - Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# - Write a program that prints the numbers from 1 to 100.
# - For multiples of three print "Fizz" instead of the number
# - For the multiples of five print "Buzz".
# - For numbers which are multiples of both three and five print "FizzBuzz".

for x in range(1, 101):
    if x % 3 == 0 and x % 5. == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)

# 4. Display a table of powers.
# 
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.


user_input = int(input("What number would you like to go up to? "))

print()
print("number | squared | cubed")
print("------ | ------- | -----")
for i in range(1, user_input + 1):
    print("%6d | %7d | %5d" % (i, i ** 2, i ** 3))

while True:
    numeric_grade = int(input("Please enter a number grade: "))

    if numeric_grade >= 97:
        print("A+")
    elif numeric_grade >= 91:
        print("A")
    elif numeric_grade >= 88:
        print("A-")
    elif numeric_grade >= 86:
        print("B+")
    elif numeric_grade >= 83:
        print("B")
    elif numeric_grade >= 80:
        print("B-")
    elif numeric_grade >= 77:
        print("C+")
    elif numeric_grade >= 72:
        print("C")
    elif numeric_grade >= 67:
        print("C-")
    elif numeric_grade >= 65:
        print("D+")
    elif numeric_grade >= 62:
        print("D")
    elif numeric_grade >= 60:
        print("D-")
    else:
        print("F")
    wants_to_continue = input("Do you want to continue? y or n. ")
    if not wants_to_continue.lower().startswith("y"):
        break

#.  Create a list of dictionaries where each dictionary represents a book that you have read. 
#.  Each dictionary in the list should have the keys title, author, and genre. 
#.  Loop through the list and print out information about each book.

#.  Prompt the user to enter a genre, 
#.  then loop through your books list and print out the titles of all the books in that genre.

