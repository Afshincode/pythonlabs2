# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1


number_list = []
for i in range(10):
    number = int(input("Enter a number: "))
    number_list.append(number)

print(f"{number_list[1], number_list[3], number_list[5], number_list[7], number_list[9]}")
print(f"{number_list[8], number_list[6], number_list[4], number_list[2], number_list[0]}")