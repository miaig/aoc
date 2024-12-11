testing = False
import re

fileinput = ""

#######################
# testing = True
#######################

if testing:
    file = 'test-input.txt'
else:
    file = 'input.txt'
with open(file, 'r') as file:  # Replace 'input.txt' with your file name
    for line in file:
        fileinput += line

pattern = r"mul\((\d+),(\d+)\)" 
filtered = re.findall(pattern, fileinput)
output = 0

for val in filtered:
    a = int(val[0])
    b = int(val[1])

    output += (a*b)
# print(type(output))
print(output)
