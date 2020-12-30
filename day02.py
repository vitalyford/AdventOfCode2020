answer1, answer2 = 0, 0


with open("input/day02.in", "r") as f:
    lines = f.readlines()
    for line in lines:
        split = line.split(' ')
        min, max = map(int, split[0].split('-'))
        
        c = split[2].count(split[1][0])
        if c <= max and c >= min:
            answer1 += 1
        if (split[2][min-1] == split[1][0]) ^ (split[2][max-1] == split[1][0]):
            answer2 += 1


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
