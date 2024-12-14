from os import sched_rr_get_interval


testing = False

fileinput = []
numbers = []
sizex = 0
sizey = 0

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def getpos(self):
        print(f"X: {self.x}    Y: {self.y}")

    def getq(self):
        if self.x == sizex // 2:
            return -1
        elif self.x < sizex // 2:
            xq = 0
        else:
            xq = 1

        if self.y == sizey // 2:
            return -1
        elif self.y <= sizey // 2:
            yq = 0
        else:
            yq = 1

        # print(xq, yq)
        if   (xq == 0) and (yq == 0):
            return 0
        elif (xq == 1) and (yq == 1):
            return 3
        elif (xq == 0) and (yq == 1):
            return 2
        elif (xq == 1) and (yq == 0):
            return 1
        else:
            return -2

    def move(self, times):
        for i in range(times):
            if self.vx >= 0:
                if self.x + self.vx < sizex:
                    self.x += self.vx
                else:
                    diff = sizex - self.x
                    movex = self.vx - diff
                    self.x = movex - 0
            else:
                if self.x + self.vx >= 0:
                    self.x += self.vx
                else:
                    diff = 0 - self.x
                    movex = diff - self.vx
                    self.x = sizex - movex


            if self.vy >= 0:
                if self.y + self.vy < sizey:
                    self.y += self.vy
                else:
                    diff = sizey - self.y
                    movey = self.vy - diff
                    self.y = movey - 0

            else:
                if self.y + self.vy >= 0:
                    self.y += self.vy
                else:
                    diff = 0 - self.y
                    movey = diff - self.vy
                    self.y = sizey - movey

#######################
# testing = True
#######################

if testing:
    file = 'test-input.txt'
    sizex = 11
    sizey = 7
else:
    file = 'input.txt'
    sizex = 101
    sizey = 103
with open(file, 'r') as file: 
    for line in file:
        fileinput.append(line.strip())

# print(fileinput)

# Source: https://stackoverflow.com/a/49556852
for s in fileinput:
    # print(s)
    newstr = ''.join((ch if ch in '0123456789-' else ' ') for ch in s)
    numbers.append([int(i) for i in newstr.split()])
# print(numbers)

# r1 = Robot(3, 0, -2, -2)
# r1.getpos()
# for i in range(40):
#     r1.move(1)
#     r1.getpos()
# print(r1.getq())

# Robot(2, 4, 2, -3).getpos()
score = [0, 0, 0, 0]
for i in range(len(numbers)):
    # print(numbers[i])
    r = Robot(numbers[i][0], numbers[i][1], numbers[i][2], numbers[i][3])
    # r.getpos()
    r.move(100)
    # r.getpos()
    if r.getq() >= 0:
        score[r.getq()] += 1
    # print(r.getq())
    # print()
print(score)
res = score[0]*score[1]*score[2]*score[3]
print(res)


