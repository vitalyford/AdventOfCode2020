answer1, answer2 = 0, 0


def has_golden(bag_name: str, bags: dict) -> int:
    if bag_name not in bags:
        return 0
    for item in bags[bag_name]:
        if 'shiny gold' in item or has_golden(item[2:], bags) == 1:
            return 1
    return 0


def calc_bags(bag_name: str, bags: dict):
    sum = 0
    for item in bags[bag_name]:
        if item != 'no other bag':
            sum += int(item[:1]) * calc_bags(item[2:], bags) + int(item[:1])
        else:
            return 0
    return sum


with open("input/day07.in", "r") as f:
    lines = f.readlines()
    bags = {}
    
    for line in lines:
        pair = line.strip().split('s contain ')
        bags[pair[0]] = [bag.strip('.s') for bag in pair[1].split(', ')]

    for bag_name in bags:
        answer1 += has_golden(bag_name, bags)
    
    answer2 = calc_bags('shiny gold bag', bags)


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
