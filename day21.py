from collections import defaultdict


answer1, answer2 = 0, []


with open("input/day21.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    all_foods = defaultdict(int)
    allergens = defaultdict(set)

    [allergens[a] for line in lines for a in line[:-1].split(' (contains ')[1].split(', ')]

    for line in lines:
        foods = set(line[:-1].split(' (contains ')[0].split(' '))
        allergs = line[:-1].split(' (contains ')[1].split(', ')
        for f in foods: all_foods[f] += 1
        for a in allergs:
            if not allergens[a]:  # allergen's set is still empty
                allergens[a].update(foods)
            else:
                allergens[a].intersection_update(foods)

    visited = set()
    while True:
        has_change = False
        for a in allergens:
            if len(allergens[a]) == 1 and a not in visited:
                visited.add(a)
                for r in allergens:
                    if r not in visited:
                        allergens[r] = allergens[r].difference(allergens[a])
                        has_change = True
        if not has_change:
            break

    answer1 = sum([all_foods[f] for f in all_foods if f not in [list(allergens[a])[0] for a in allergens]])
    answer2 = ','.join([pair[1] for pair in sorted([(a, list(f)[0]) for a, f in allergens.items()], key=lambda x: x[0])])


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
