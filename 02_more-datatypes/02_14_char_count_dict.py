# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}


text = input("Enter a text: ")

dict_ = {}
for char in text:
    dict_[char] = text.count(char)

print(dict_)    