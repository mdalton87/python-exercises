# You have rented some movies for your kids: 
#      The little mermaid (for 3 days), 
#      Brother Bear (for 5 days, they love it)
#      Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

little_mermaid_rental = dict(title="The Little Mermaid", days_rented=3)
brother_bear_rental = dict(title="Brother Bear", days_rented=5)
hercules_rental = dict(title="Hercules", days_rented=1)

print("$",(little_mermaid_rental["days_rented"] + brother_bear_rental["days_rented"] + hercules_rental["days_rented"] ) * 3)


# Suppose you're working as a contractor for 3 companies that pay you a different rate per hour.
#      Google - 400 dollars per hour
#      Amazon - 380 dollars per hour
#      Facebook - 350 dollars per hour
# How much will you receive in payment for this week? You worked: 
#      6 hours for Google
#      4 hours for Amazon
#      10 hours for Facebook

google = 400
amazon = 380
facebook = 350

print(6 * google + 4 * amazon + 10 * facebook)

#   A student can be enrolled to a class only 
#   if the class is not full 
#   and the class schedule does not conflict with her current schedule.
class_has_room = True
schedule_works = False
can_be_enrolled = class_has_room and schedule_works

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

premium_member = True
more_than_two_items = False
offer_valid = True

offer_can_be_applied = offer_valid and (premium_member or more_than_two_items)



# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_length = len(password) >= 5
username_length = len(username) <= 20
not_same = password != username
password_has_whitespace = password == password.strip()
username_has_whitespace = username == username.strip()


print(password_length)
print(username_length)
print(not_same)

good_username_and_password = ( password_length
                                and username_length
                                and not_same
                                and password_has_whitespace
                                and username_has_whitespace)



