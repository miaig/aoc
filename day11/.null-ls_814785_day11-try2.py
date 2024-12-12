testing = False

fileinput = ""

#######################
testing = True
#######################

if testing:
    file = 'test-input.txt'
else:
    file = 'input.txt'
with open(file, 'r') as file:  # Replace 'input.txt' with your file name
    for line in file:
        fileinput = line.split()

print(fileinput)
for times in range(6):
    skipnext = False
    for i in range(len(fileinput)+1):
        # print(skipnext)
        if skipnext:
            skipnext = False
            continue
        print(fileinput[i])
        # print("i executed")
        # print(len(fileinput[i]))
        # print(len(fileinput) + 1)
        if fileinput[i] == '0':
            fileinput[i] = '1'
            # print("0")
        elif (len(fileinput[i]) % 2) == 0:
            # print("%2")
            left = str(int(fileinput[i][:(int(len(fileinput[i]) / 2 ))]))
            right = str(int(fileinput[i][(int(len(fileinput[i]) / 2 )):]))
            # print(f"L:{left} R:{right}")
            fileinput[i] = left
            fileinput.insert(i+1,right)
            # print(fileinput)
            # i += 1
            skipnext = True
            # continue
        else: #if not (fileinput[i] == '0' and (len(fileinput[i]) % 2) == 0):
            # print("2024")
            # print(fileinput[i])
            # print(int(fileinput[i]))
            fileinput[i] = str(int(fileinput[i]) * 2024)
        # print(skipnext)
    print(fileinput)
