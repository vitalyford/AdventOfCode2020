answer1, answer2 = '', 1


# solve the first puzzle
with open("input/day23.in", "r") as f:
    cups = [int(n) for n in f.readline().strip()]

    min_cup, max_cup = min(cups), max(cups)

    curr = 0

    for _ in range(100):
        label = cups[curr]
        r = []
        i = curr + 1
        for _ in range(3):
            if i >= len(cups):
                i = 0
            r.append(cups.pop(i))
        
        dst = label - 1
        while dst in r or dst < min_cup:
            dst -= 1
            if dst < min_cup:
                dst = max_cup

        for i, c in enumerate(cups):
            if c == dst:
                cups = cups[:i + 1] + r + cups[i + 1:]
                break
        
        curr = (cups.index(label) + 1) % len(cups)
    
    for i, c in enumerate(cups):
        if c == 1:
            final = i
            i = (i + 1) % len(cups)
            while i != final:
                answer1 += str(cups[i])
                i = (i + 1) % len(cups)
            break


# solve the second puzzle
with open("input/day23.in", "r") as f:
    ins = [int(n) for n in f.readline().strip()]
    for i in range(10, 1000001):
        ins.append(i)

    min_cup, max_cup = 1, 1000000

    cups = [0] * 1000001
    for i in range(len(ins) - 1):
        cups[ins[i]] = ins[i + 1]
    cups[ins[i + 1]] = ins[0]

    label = ins[0]

    for k in range(10000000):
        r = []
        curr = cups[label]
        for _ in range(3):
            r.append(curr)
            curr = cups[curr]
        cups[label] = curr

        dst = label - 1
        while dst in r or dst < min_cup:
            dst -= 1
            if dst < min_cup:
                dst = max_cup

        last       = cups[dst]
        cups[dst]  = r[0]
        cups[r[0]] = r[1]
        cups[r[1]] = r[2]
        cups[r[2]] = last
        label      = cups[label]

    answer2 = cups[1] * cups[cups[1]]


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
