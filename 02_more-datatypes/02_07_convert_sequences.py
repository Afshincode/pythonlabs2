# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

tuple_ = tuple(string)
print(tuple_)

list_ = list(tuple_)
print(list_)

list_[0] = 'k'
print(list_)

new_tuple = tuple(list_)
print(new_tuple)