testing = True

matrix = []

if testing:
    file = 'test-input.txt'
else:
    file = 'input.txt'
with open(file, 'r') as file:  # Replace 'input.txt' with your file name
    for line in file:
        # Split the line into two values
        row = list(map(int, line.split()))
        
        # Append to respective lists
        matrix.append(row)


# Print the results
print(matrix)

# output = 0
# for i in range(len(left_list)):
#     amount = 0
#     for j in range(len(right_list)):
#         if left_list[i] == right_list[j]:
#             amount += 1
#     output += left_list[i] * amount
# print(output)

# print(matrix[0][0])

# safe = 0
# for i in range(len(matrix)):
#     if matrix[i][0] > matrix [i][1]: #increasing
#         unsafe = False
#         for j in range(len(matrix[i]) - 1):
#             if (matrix[i][j] > matrix[i][j+1]) and (1 < abs(matrix[i][j] - matrix[i][j+1]) < 4 and not unsafe):
#                 print(matrix[i])
#                 pass
#                 # safe += 1
#                 # print("correct: ", matrix[i])
#             else:
#                 unsafe = True
#         if not unsafe:
#             print(matrix[i])
#
#     elif matrix[i][0] < matrix [i][1]: #decreasing
#         unsafe = False
#         for j in range(len(matrix[i]) - 1):
#             if (matrix[i][j] < matrix[i][j+1]) and (1 < abs(matrix[i][j] - matrix[i][j+1]) < 4 and not unsafe):
#                 print(matrix[i])
#                 pass
#                 # safe += 1
#                 # print("correct:", matrix[i])
#             else:
#                 unsafe = True
#         if not unsafe:
#             safe += 1
#             print(matrix[i])
#
# print(safe)


safe = 0
for i in range(len(matrix)):
    bsafe = True
    trend = 0
    error = 0
    for j in range(len(matrix[i]) - 1):
        diff = matrix[i][j+1] - matrix[i][j]
        if (1 <= diff <= 3): #increasing
            if trend == 0:
                trend = 1
            elif trend == -1:
                error += 1
        elif (-3 <= diff <= -1):
            if trend == 0:
                trend = -1
            elif trend == 1:
                error += 1
        else:
            error += 1

    if error <= 0:
        print(matrix[i])
        safe += 1

print(safe)
