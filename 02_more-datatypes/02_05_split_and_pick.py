# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

text = input("Enter a sentence: ")
list_of_words = text.split()


most_common_word = ""
highest_count = 0

for word in list_of_words:
    if text.count(word) > highest_count:
        most_common_word = word
        highest_count = text.count(word)

print(most_common_word)
