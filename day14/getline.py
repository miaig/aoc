import re

input = 'output.txt'

longest_sequence = 0
line_with_longest = None

with open(input, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        matches = re.findall(r'#+', line)
        if matches:
            max_length_in_line = max(len(match) for match in matches)
            if max_length_in_line > longest_sequence:
                longest_sequence = max_length_in_line
                line_with_longest = line_number

print(longest_sequence)
