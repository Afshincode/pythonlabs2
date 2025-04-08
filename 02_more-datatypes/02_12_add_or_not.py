# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.


set_ = set()
points = 5
while points > 0:
    number = input("Enter a number: ")
    if number.isdigit():
        number = int(number)
        if len(set_) == 9:
            print("Congratulations, you won the game!")
            break
        elif number in set_:
            print("Your input is a duplicate, you lost a point.")
            points -= 1
        else:
            set_.add(number)     
    else:
        print("You should enter a number.")


