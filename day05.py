import math


answer1, answer2 = 0, 0
ids = []


with open("input/day05.in", "r") as f:
    lines = f.readlines()
    for line in lines:
        row_low, row_high  = 0, 127
        col_low, col_high = 0, 7

        for c in line:
            if c == 'F':
                row_high = math.floor((row_high + row_low) / 2)
            elif c == 'B':
                row_low  = math.ceil ((row_high + row_low) / 2)
            elif c == 'L':
                col_high = math.floor((col_high + col_low) / 2)
            elif c == 'R':
                col_low  = math.ceil ((col_high + col_low) / 2)

        answer1 = max(row_low * 8 + col_low, answer1)

        ids.append(row_low * 8 + col_low)


ids = sorted(ids)


for i in range(1, len(ids)):
    if ids[i] - ids[i - 1] == 2:
        answer2 = ids[i] - 1
        break


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
