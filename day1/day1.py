import math
# Open the input file
left_list = []
right_list = []

with open('day1-input.txt', 'r') as file:  # Replace 'input.txt' with your file name
    for line in file:
        # Split the line into two values
        left, right = map(int, line.split())
        
        # Append to respective lists
        left_list.append(left)
        right_list.append(right)

# left_list.sort()
# right_list.sort()

# Print the results
print("Left List:", left_list)
print("Right List:", right_list)

# diff = 0
# for i in range(len(left_list)):
#     diffu = left_list[i] - right_list[i]
#     diff += math.sqrt(diffu * diffu)
#     print(diff)
#     pass

output = 0
for i in range(len(left_list)):
    amount = 0
    for j in range(len(right_list)):
        if left_list[i] == right_list[j]:
            amount += 1
    output += left_list[i] * amount
    print(output)
