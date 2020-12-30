nums = set()
answer1, answer2 = -1, -1


with open("input/day01.in", "r") as f:
    lines = f.readlines()
    for line in lines:
        n = int(line)
        if 2020 - n in nums:
            answer1 = n * (2020 - n)
        nums.add(n)

for i in nums:
    for j in nums:
        if 2020 - i - j in nums:
            answer2 = i * j * (2020 - i - j)


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
