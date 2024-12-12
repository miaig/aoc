testing = False

fileinput = []

#######################
# testing = True
#######################

if testing:
    file = 'test-input.txt'
else:
    file = 'input.txt'
with open(file, 'r') as file:  # Replace 'input.txt' with your file name
    for line in file:
        fileinput.append(line.split())
#
# print(fileinput)
# for times in range(6):
#     for i in range(len(fileinput[times])):
#         print(i)
#         print(fileinput[times][i])
#         # print("i executed")
#         # print(len(fileinput[i]))
#         # print(len(fileinput) + 1)
#         if fileinput[times][i] == '0':
#             fileinput[times+1][i] = '1'
#             # print("0")
#         elif (len(fileinput[times][i]) % 2) == 0:
#             # print("%2")
#             left = str(int(fileinput[times][i][:(int(len(fileinput[times][i]) / 2 ))]))
#             right = str(int(fileinput[times][i][(int(len(fileinput[times][i]) / 2 )):]))
#             # print(f"L:{left} R:{right}")
#             fileinput.append(left)
#             fileinput.append(right)
#             # print(fileinput)
#             # i += 1
#             # continue
#         else: #if not (fileinput[i] == '0' and (len(fileinput[i]) % 2) == 0):
#             # print("2024")
#             # print(fileinput[i])
#             # print(int(fileinput[i]))
#             fileinput[times].append(str(int(fileinput[times][i]) * 2024))
#         # print(skipnext)
#     print(fileinput)


# print("fileinput",fileinput)
inters = 25
for times in range(inters):
    fileinput.append([])
    # print("len(fileinput[times])",len(fileinput[times]))
    for i in range(len(fileinput[times])):
        # print("fileinput[times][i]",fileinput[times][i])
        if fileinput[times][i] == '0':
            fileinput[times+1].append('1')
            # print("fileinput1",fileinput)
        elif len(fileinput[times][i]) % 2 == 0:
            left = str(int(fileinput[times][i][:(int(len(fileinput[times][i]) / 2 ))]))
            right = str(int(fileinput[times][i][(int(len(fileinput[times][i]) / 2 )):]))
            fileinput[times+1].append(left)
            fileinput[times+1].append(right)
            # print("fileinput2",fileinput)
        else:
            fileinput[times+1].append(str(int(fileinput[times][i]) * 2024))
            # print("fileinput3",fileinput)

print(f"\n\n{len(fileinput[inters])}")
