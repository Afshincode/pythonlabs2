# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!


input_dict = {"item1": 5, "item2": 6, "item3": 1}

list_ = []
for key, Value in input_dict.items():
    tuple_ = (key, Value)
    list_.append(tuple_)

result_list = sorted(list_, key=lambda item: item[1])
print(result_list)
