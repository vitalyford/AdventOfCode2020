from collections import defaultdict 


answer1, answer2 = 0, 0


with open("input/day06.in", "r") as f:
    lines = f.readlines()
    q = defaultdict(int)
    count = 0
    for line in lines:
        line = line.strip()
        if line == '':
            answer1 += len(q)
            for k, v in q.items():
                if v == count:
                    answer2 += 1
            q = defaultdict(int)
            count = 0
            continue
        for c in line:
            q[c] += 1
        count += 1


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
