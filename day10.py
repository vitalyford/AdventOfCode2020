from collections import defaultdict 


answer1, answer2 = 0, 0


def count_arrangements(lines: list) -> int:
    counts = [1]
    for i in range(1, len(lines)):
        sum = 0
        for j in range(1, 4):
            if i - j >= 0 and lines[i] - lines[i - j] <= 3:
                sum += counts[i - j]
        counts.append(sum)
    return counts[-1]


with open("input/day10.in", "r") as f:
    lines = sorted([int(line) for line in f.readlines()] + [0])

    lines.append(lines[-1] + 3)

    diffs = defaultdict(int)
    for i in range(1, len(lines)):
        diffs[lines[i] - lines[i - 1]] += 1
    
    answer1 = diffs[1] * diffs[3]

    answer2 = count_arrangements(lines)


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
