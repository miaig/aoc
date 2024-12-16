testing = False
import re

fileinput = ""
do = []
dont = []
number_indexes = []

#######################
# testing = True
#######################

if testing:
    file = 'test-input.txt'
else:
    file = 'input.txt'
with open(file, 'r') as file: 
    for line in file:
        fileinput += line

pattern = r'mul\((\d+),(\d+)\)' 
patdo = r'do\(\)'
patdont = r'don\'t\(\)'
filtered = re.findall(pattern, fileinput)
for match in re.finditer(pattern, fileinput):
    number_indexes.append(match.start())
# filtered = re.finditer(pattern, fileinput)
for match in re.finditer(patdo, fileinput):
    do.append(match.start())
for match in re.finditer(patdont, fileinput):
    dont.append(match.start())
output = 0

# print(fileinput, end='')
# print(filtered)
# for match in ifiltered:
#     print(match.start(), match.group())
# print(do)
# for match in ido:
#     print(match.start(), match.group())
# print(dont)
# for match in idont:
#     print(match.start(), match.group())
# for val in filtered:
#     a = int(val[0])
#     b = int(val[1])
#
#     output += (a*b)
# print(output)

# print(type(ido))
enabled = True
count = 0
for i in range(len(fileinput)):
    if i in do:
        enabled = True
    if i in dont:
        enabled = False
    if i in number_indexes:
        if enabled:
            output += (int(filtered[count][0]) * int(filtered[count][1]))
        count += 1
    # if i in ifiltered:
    #     if enabled:
    #         for val in filtered:
    #             print(val)
    #             a = int(val[0])
    #             b = int(val[1])
    #
    #             output += (a*b)

print(output)


# for i in range(len(fileinput)):
#     for match in ido:
#         if i == match.start():
#             print("sfoh")
#         print(match.start(), match.group())
#     for match in idont:
#         print(match.start(), match.group())

# enabled = True
# for match in ido:
#     for i in range(len(fileinput)):
#         if i == match.start():
#             enabled = True
#             print("hie", i, match)

# for i in range(len(fileinput)):
#     for match in idont:
#         val = match.start()
#     #     # print(match.start(), match.group())
#         # print(i, end=' ')
#         print(val)
#         # if int(val) == int(i):
#         #     print("hi")
#         # else:
#         #     pass
#     
#     print(i)
