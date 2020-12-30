answer1, answer2 = 0, 0


def count_active_mini(space: dict, xi: int, yi: int, zi: int, wi: int) -> int:
    active = 0
    for x in range(xi - 1, xi + 2):
        for y in range(yi - 1, yi + 2):
            for z in range(zi - 1, zi + 2):
                for w in range(wi - 1, wi + 2):
                    if x in space and y in space[x] and z in space[x][y] and w in space[x][y][z] and space[x][y][z][w] == '#':
                        active += 1
    return active


def change_status(space: dict, xi: int, yi: int, zi: int, wi: int, v: int) -> dict:
    new_space = {}
    active = 0
    for x in range(xi - 1, xi + 2):
        for y in range(yi - 1, yi + 2):
            for z in range(zi - 1, zi + 2):
                for w in range(wi - 1, wi + 2):
                    if x in space and y in space[x] and z in space[x][y] and w in space[x][y][z] and space[x][y][z][w] == '#':
                        active += 1
    if v == '#':
        return '#' if active == 3 or active == 4 else '.'
    else:
        return '#' if active == 3 else '.'


def count_active(space: dict) -> int:
    active = 0
    for x in space:
        for y in space[x]:
            for z in space[x][y]:
                for w in space[x][y][z]:
                    if space[x][y][z][w] == '#':
                        active += 1
    return active


with open("input/day17.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    space = {}
    x, z, w = -1, 0, 0
    for row in range(len(lines)):
        space[x] = {}
        y = -1
        for col in range(len(lines[0])):
            space[x][y] = { z: { w: lines[row][col] } }
            y += 1
        x += 1
    
    for _ in range(6):
        new_space = {}
        visited = set()
        for xi in space:
            if xi not in new_space: new_space[xi] = {}
            for yi in space[xi]:
                if yi not in new_space[xi]: new_space[xi][yi] = {}
                for zi in space[xi][yi]:
                    if zi not in new_space[xi][yi]: new_space[xi][yi][zi] = {}
                    for wi in space[xi][yi][zi]:
                        for x in range(xi - 1, xi + 2):
                            if x not in new_space: new_space[x] = {}
                            for y in range(yi - 1, yi + 2):
                                if y not in new_space[x]: new_space[x][y] = {}
                                for z in range(zi - 1, zi + 2):
                                    if z not in new_space[x][y]: new_space[x][y][z] = {}
                                    for w in range(wi - 1, wi + 2):
                                        # if w not in new_space[x][y][z]: new_space[x][y][z][w] = {}
                                        if (x, y, z, w) not in visited:
                                            new_space[x][y][z][w] = change_status(space, x, y, z, w, space[x][y][z][w] if x in space and y in space[x] and z in space[x][y] and w in space[x][y][z] else '.')
                                            visited.add((x, y, z, w))
        space = new_space
    
    # added forth dimension so answer1 no longer works
    # but it's easy to get back to three dimensions
    # answer1 = count_active(space)
    answer2 = count_active(space)
    

print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
