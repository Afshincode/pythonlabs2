# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.


def make_sandwich(bread, *toppings):
    if toppings:
        all_toppings = ""
        for topping in toppings:
            all_toppings += f"{topping}, " 
        sandwich = f"{bread} sandwich with {all_toppings}"
    else:
        sandwich = f"{bread} sandwich with no toppings"

    return sandwich

sandwich1 = make_sandwich("whole weat", "lettuce", "cheese")
print(sandwich1)
sandwich2 = make_sandwich("whole wheat")
print(sandwich2)