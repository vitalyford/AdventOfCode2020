answer1, answer2 = 0, 0


def recursive_combat(p1: list, p2: list) -> int:
    prev_rounds = set()
    winner = 0

    while True:
        if (tuple(p1), tuple(p2)) in prev_rounds:
            return 1
        prev_rounds.add((tuple(p1[:]), tuple(p2[:])))

        d1 = p1.pop(0)
        d2 = p2.pop(0)

        if len(p1) >= d1 and len(p2) >= d2:
            winner = recursive_combat(p1[:d1], p2[:d2])
        else:
            winner = 1 if d1 > d2 else 2
        
        if winner == 1:
            p1.extend([d1, d2])
        elif winner == 2:
            p2.extend([d2, d1])

        if len(p1) == 0 or len(p2) == 0:
            return 1 if p1 else 2


with open("input/day22.in", "r") as f:
    p1 = []

    f.readline()
    while True:
        line = f.readline().strip()
        if not line:
            break
        p1.append(int(line))
    
    f.readline()
    p2 = [int(line.strip()) for line in f.readlines()]

    p1_2, p2_2 = p1[:], p2[:]

    while p1 and p2:
        if p1[0] > p2[0]:
            p1.extend([p1.pop(0), p2.pop(0)])
        else:
            p2.extend([p2.pop(0), p1.pop(0)])

    winner = p1 if p1 else p2
    answer1 = sum([a * (i + 1) for i, a in enumerate(winner[::-1])])

    recursive_combat(p1_2, p2_2)
    winner = p1_2 if p1_2 else p2_2
    answer2 = sum([a * (i + 1) for i, a in enumerate(winner[::-1])])


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
