from collections import defaultdict


answer1, answer2 = 0, 0


def verify_tickets(rules: dict, nearby_t: list) -> int:
    sum = 0
    valid_t = []
    for t in nearby_t:
        all_nums_valid = True
        for n in t:
            # checking the individual number (n) against the rules
            verified = False
            for rule in [r for rule in rules.values() for r in rule]:
                if rule[0] <= n <= rule[1]:
                    verified = True
                    break
            if not verified:
                all_nums_valid = False
                sum += n
        if all_nums_valid:
            valid_t.append(t)
    return sum, valid_t


def remove(pos: defaultdict, num: int) -> None:
    for k, v in pos.items():
        if len(v) != 1:
            pos[k] = list(filter(lambda n: n != num, v))


def multiply_departures(rules: dict, nearby_t: list, t_len: int, my_t: list) -> int:
    pos = defaultdict(list)
    # find possible positions for the rules
    for rule_name, rule in rules.items():
        for i in range(t_len):
            all_t_good = True
            for t in nearby_t:
                good_pos = False
                for r in rule:
                    if r[0] <= t[i] <= r[1]:
                        good_pos = True
                        break
                if not good_pos:
                    all_t_good = False
                    break
            if all_t_good:
                pos[rule_name].append(i)
    while True:
        for k, v in pos.items():
            if len(v) == 1:
                remove(pos, v[0])
        sum = 0
        for p in pos.values():
            sum += len(p)
        if sum == len(pos):
            break
    
    prod = 1
    for k, v in pos.items():
        if 'departure' in k:
            prod *= my_t[v[0]]

    return prod


with open("input/day16.in", "r") as f:
    # read the rules
    rules = {}
    line = f.readline().strip()
    while line != '':
        rules[line.split(':')[0]] = [(int(pair.split('-')[0]), int(pair.split('-')[1])) for pair in line.split(': ')[1].split(' or ')]
        line = f.readline().strip()
    
    # read my ticket
    f.readline()
    my_t = list(map(int, f.readline().strip().split(',')))
    f.readline()

    # read the nearby tickets
    f.readline()
    nearby_t = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        nearby_t.append(list(map(int, line.split(','))))
    
    answer1, valid_t = verify_tickets(rules, nearby_t)

    answer2 = multiply_departures(rules, valid_t, len(my_t), my_t)


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
