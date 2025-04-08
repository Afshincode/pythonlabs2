# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.


def show_advertisement(**kwargs):
    print("Real state advertisement:\n")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_advertisement(price="$100000", bedrooms=2, size=100)