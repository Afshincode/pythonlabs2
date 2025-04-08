# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list_of_numbers):
  # define the function here
  maixmum = max(list_of_numbers)
  minimum = min(list_of_numbers)
  sum_of_numbers = sum(list_of_numbers)
  average = sum_of_numbers / len(list_of_numbers)
  return maixmum, minimum, sum_of_numbers, average

# call the function below here

result = stats(example_list)
print(f"Maximum:{result[0]}")
print(f"Minimum: {result[1]}")
print(f"Sum: {result[2]}")
print(f"Average: {result[3]}")