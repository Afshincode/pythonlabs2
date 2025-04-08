# Add the code for the file counter script that you wrote in the course.
import csv
import pathlib


desktop = pathlib.Path('/Users/Afshin2/Desktop')


suffixes = []
for filepath in desktop.iterdir():    
    suffixes.append(filepath.suffix)
unique_suffixes = set(suffixes)

count = {}
for item in unique_suffixes:
    count[item] = suffixes.count(item)

# file_out = open("filecounts.txt", "w")
# file_out.write(str(count))
# file_out.write("\n")
# file_out.close()

# file_in = open("filecounts.txt", "r")
# contents = file_in.read()
# file_in.close()

with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count['.lnk'], count['.jpeg'], count['.txt'], count['.py'], count['.ini']]
    countwriter.writerow(data)