# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.



def greet(greeting, name):
    """Generates a greeting."""
    sentence = f"{greeting}, {name}! How are you?"
    return sentence


def write_letter(name, text):
    greeting = greet("Hello", name)
    goodbye = f"Goodbye {name}"
    return greeting + text + " " + goodbye


print(write_letter("Afshin", "It's a nice day."))