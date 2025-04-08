# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """
    This function converts km to miles
    It take a number in km and return a number in miles
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)

