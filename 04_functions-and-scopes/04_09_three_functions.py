# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.


def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average

def display_results(numbers):
    total_sum = calculate_sum(numbers)
    average = calculate_average(numbers)

    print(f"Sum of numbers: {total_sum}")
    print(f"Average of numbers: {average}")


display_results([1,2,3,4,5,6,7])