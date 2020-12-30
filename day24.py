import math, copy
from collections import defaultdict


answer1, answer2, precision = 0, 0, 3


def calc(line: str, d: dict) -> tuple:
    i = 0
    s = (0, 0)
    while i < len(line):
        k = line[i:i+1] if line[i:i+1] in d else line[i:i+2]
        i = i + 1 if len(k) == 1 else i + 2
        s = tuple(map(lambda i, j: i + j, s, d[k]))
    return (round(s[0], precision), round(s[1], precision))


def is_nearby(t1: tuple, t2: tuple, s3: float) -> bool:
    return abs(s3 - math.sqrt((t1[0] - t2[0]) * (t1[0] - t2[0]) + (t1[1] - t2[1]) * (t1[1] - t2[1]))) < 0.1


def expand(tiles: dict, d: dict, s3: float) -> None:
    new_tiles = defaultdict(bool)

    for t in tiles:
        for k in d:
            # the tile need to be black to add surrounding tiles
            if tiles[t]:
                s = tuple(map(lambda i, j: round(i + j, precision), t, d[k]))
                if s not in tiles and s not in new_tiles:
                    new_tiles[s] = False

    tiles.update(new_tiles)


with open("input/day24.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    s3 = round(math.sqrt(3), precision)
    d = { 'w': (-s3, 0), 'nw': (-s3 / 2.0, 1.5), 'ne': (s3 / 2.0, 1.5), 'e': (s3, 0), 'se': (s3 / 2.0, -1.5), 'sw': (-s3 / 2.0, -1.5) }

    tiles = defaultdict(bool)

    for line in lines:
        tiles[calc(line, d)] = not tiles[calc(line, d)]
    
    # black tile is true, white is false
    answer1 = sum([1 for t in tiles if tiles[t]])  

    for p in range(100):
        expand(tiles, d, s3)
        t = copy.deepcopy(tiles)
        for i in tiles:
            count = 0
            for _, c in d.items():
                j = (round(i[0] + c[0], precision), round(i[1] + c[1], precision))
                count = count + 1 if i != j and j in tiles and tiles[j] else count
            # if the tile is black
            if tiles[i] and (count == 0 or count > 2):
                t[i] = False  # make white
            # the tile is white
            elif not tiles[i] and count == 2:
                t[i] = True   # make black
        tiles = copy.deepcopy(t)
        print('2020 is tough, no time to optimize this puzzle, gotta wait ' + str(p) + '/100 ' + ' with tiles size = ' + str(len(tiles)))

    answer2 = sum([1 for t in tiles if tiles[t]])
    

print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
