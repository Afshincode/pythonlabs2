# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here

randlist.sort()


start = 0
end = 2
new_list = []
if len(randlist) % 2 == 0:
    for i in range(int(len(randlist) / 2)):
        tuple_ = tuple(randlist[start:end])
        new_list.append(tuple_)
        start += 2
        end += 2
else:
    for i in range(int(len(randlist) // 2)):
        tuple_ = tuple(randlist[start:end])
        new_list.append(tuple_)
        start += 2
        end += 2
    last_number = randlist.pop()
    last_list = [last_number, 0]
    new_list.append(tuple(last_list))

for item in new_list:
    print(item)
    
    
