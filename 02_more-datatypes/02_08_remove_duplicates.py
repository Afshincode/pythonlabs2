# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# first way
set_ = set(list_)
new_list_ = list(set_)
print(new_list_)

# second way
new_list_ = []
for item in list_:
    if item not in new_list_:
        new_list_.append(item)
print(new_list_)