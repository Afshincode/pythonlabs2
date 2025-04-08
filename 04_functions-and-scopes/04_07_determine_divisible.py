# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages


def is_divisible(number):
    return number % 4 == 0 or number % 7 == 0

def is_divisible_both(number):
    return number % 4 == 0 and number % 7  == 0

user_number = int(input("Enter a number between 1 and 1,000,000,000: "))
one_divisible = is_divisible(user_number)
both_divisible = is_divisible_both(user_number)

if one_divisible:
    print(f"{user_number} is divisible by 4 or 7.")
else:
    print(f"{user_number} is not divisible by 4 or 7.")

if both_divisible:
    print(f"{user_number} is divisible by both 4 and 7.")
else:
    print(f"{user_number} is not divisible by both 4 and 7.")