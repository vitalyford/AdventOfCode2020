answer1, answer2 = 0, 0


def move(curr_pos: int, input: str, dirs: list, location: dict) -> int:
    if input[0] in dirs or input[0] == 'F':

        d = input[0]

        if input[0] == 'F':
            d = dirs[curr_pos]

        diff = location[dirs[(dirs.index(d) + 2) % 4]] - int(input[1:])
        if diff < 0:
            location[d] += abs(diff)
        
        location[dirs[(dirs.index(d) + 2) % 4]] = max(0, diff)

    elif input[0] == 'L' or input[0] == 'R':
        sign = -1 if input[0] == 'L' else 1
        curr_pos = (curr_pos + sign * int(input[1:]) // 90) % 4

    return curr_pos


with open("input/day12.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    dirs = ['E', 'S', 'W', 'N']

    # solve the first puzzle
    location = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
    curr_pos = 0  # position at East in the directions list

    for line in lines:
        curr_pos = move(curr_pos, line, dirs, location)

    answer1 = sum(location.values())
    
    # solve the second puzzle
    ship_x, ship_y = 0, 0
    way_x, way_y  = 10, 1

    for line in lines:
        if line[0] == 'F':
            ship_x += way_x * int(line[1:])
            ship_y += way_y * int(line[1:])
        elif line[0] in dirs:
            d, step = line[0], int(line[1:])
            if d == 'N':
                way_y += step
            elif d == 'S':
                way_y -= step
            elif d == 'E':
                way_x += step
            elif d == 'W':
                way_x -= step
        else:  # rotate to left or right
            if line[0] == 'R':
                for _ in range(int(line[1:]) // 90):
                    way_x, way_y = way_y, -way_x
            else:
                for _ in range(int(line[1:]) // 90):
                    way_x, way_y = -way_y, way_x
    
    answer2 = abs(ship_x) + abs(ship_y)


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
