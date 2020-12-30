from collections import defaultdict


answer1, answer2 = 0, 0


def calc(limit: int, nums: list) -> int:
    spoken      = defaultdict(list)
    turn        = 1
    i           = 0
    last_spoken = -1

    for n in nums:
        spoken[n].append(turn)
        turn += 1
    last_spoken = nums[-1]

    while turn <= limit:
        if len(spoken[last_spoken]) == 1:  # first-time spoken
            last_spoken = 0
            if len(spoken[0]) == 2:
                spoken[0][1] = spoken[0][0]
                spoken[0][0] = turn
            else:
                spoken[last_spoken].append(spoken[last_spoken][0])
                spoken[last_spoken][0] = turn
        else:
            last_spoken = spoken[last_spoken][0] - spoken[last_spoken][1]
            if last_spoken not in spoken:
                spoken[last_spoken].append(turn)
            elif len(spoken[last_spoken]) == 1:
                spoken[last_spoken].append(spoken[last_spoken][0])
                spoken[last_spoken][0] = turn
            else:
                spoken[last_spoken][1] = spoken[last_spoken][0]
                spoken[last_spoken][0] = turn
        turn += 1
    
    return last_spoken


with open("input/day15.in", "r") as f:
    nums    = list(map(int, f.readline().strip().split(',')))
    answer1 = calc(2020, nums)
    answer2 = calc(30000000, nums)


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
