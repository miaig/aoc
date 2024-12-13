testing = False
import sympy as sp

fileinput = []
tokens = 0

#######################
# testing = True
#######################

if testing:
    file = 'test-input.txt'
else:
    file = 'input.txt'
# with open(file, 'r') as file: 
#     for line in file:
#         for char in line:
#             if char.isdigit():
#                 fileinput.append(char)
#
# Code a lá Internet
with open(file, 'r') as file:
    all_Text = file.read()
numbers = []
i = 0
while i < len(all_Text):
    if all_Text[i].isdigit():
        start = i
        while i < len(all_Text) and all_Text[i].isdigit():
            i += 1
        numbers.append(int(all_Text[start:i]))
    else:
        i += 1
# print(numbers)

def calc(valxA, valxB, valyA, valyB, resX, resY):
    global tokens
    x, y = sp.symbols('x, y')
    eq1 = sp.Eq(x*valxA + y*valxB, resX)
    eq2 = sp.Eq(x*valyA + y*valyB, resY)
    ans = sp.solve((eq1, eq2), (x, y))
    # tokens =nsns[0]*3 + ans[1]
    # print(ans) # {x: 80, y: 40}
    # print(type(ans[x])) # 80
    # print(ans[y]) # 40
    # tokens = ans[x]*3 + ans[y]

    if type(ans[x]) and type(ans[x]) == sp.core.numbers.Integer:
        # print("hi")
        tokens += ans[x]*3 + ans[y]
    else:
        pass
    # print("Tokens: ", tokens, "\n")

i = 0
while i < len(numbers):
    valxA = numbers[i+0]
    valyA = numbers[i+1]
    valxB =  numbers[i+2]
    valyB = numbers[i+3]
    resX =  numbers[i+4]
    resY = numbers[i+5]
    calc(valxA, valxB, valyA, valyB, resX, resY)
    # print(valxA, valxB, valyA, valyB, resX, resY)
    i += 6
                
# print(fileinput)
# print("".join(fileinput))

print("\n\n", tokens)
