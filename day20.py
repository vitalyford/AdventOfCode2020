import copy, re


answer1, answer2 = 1, 0


class Tile:
    def try_left_right(self, pic: list, c: int) -> bool:
        # if c == 0 then it's a left, otherwise - right side
        pic_col = self.w - 1 if c == 0 else 0
        for r in range(self.h):
            if self.orig[r][c] != pic[r][pic_col]:
                return False
        return True
    
    def try_top_bottom(self, pic: list, r: int) -> bool:
        # if c == 0 then it's a top, otherwise - bottom side
        pic_row = self.h - 1 if r == 0 else 0
        for c in range(self.w):
            if self.orig[r][c] != pic[pic_row][c]:
                return False
        return True

    def vert_mirror(self, o: list) -> list:
        pic = []
        # mirror vertically
        for r in range(self.h):
            line = ''
            for c in range(1, self.w + 1):
                line += o[r][self.w - c]
            pic.append(line)
        return pic
    
    def hor_mirror(self, o: list) -> list:
        pic = []
        # mirror horizontally
        for r in range(1, self.h + 1):
            line = ''
            for c in range(self.w):
                line += o[self.h - r][c]
            pic.append(line)
        return pic

    def turn_90(self, o: list) -> list:
        pic = []
        # turn 90 degress clockwise
        for c in range(0, self.w):
            line = ''
            for r in range(self.h):
                line += o[r][c]
            pic.append(line)
        return pic

    def init_rot_flip(self) -> None:
        if self.orig:
            self.h = len(self.orig)
            self.w = len(self.orig[0])

            self.pics.append(self.orig)
            self.pics.append(self.vert_mirror(self.orig))
            self.pics.append(self.hor_mirror(self.orig))
            self.pics.append(self.hor_mirror(self.pics[1]))
            self.pics.append(self.turn_90(self.orig))
            self.pics.append(self.vert_mirror(self.pics[4]))
            self.pics.append(self.hor_mirror(self.pics[4]))
            self.pics.append(self.hor_mirror(self.pics[5]))

    def __init__(self, name: str):
        self.orig = []
        self.pics = []
        self.name = name
        self.w = 0
        self.h = 0
        self.left, self.right, self.top, self.bottom = None, None, None, None


def connect_tiles(name: str, tiles: dict) -> None:
    tile_q = []  # queue to keep track of the tiles
    vis    = set()  # visited tiles list

    tile_q.append(tiles[name])

    while len(tile_q) != 0:
        curr = tile_q.pop(0)
        if curr.name in vis: continue
        vis.add(curr.name)
        for name, tile in tiles.items():
            if name in vis: continue
            for pic in tile.pics:
                connected = False
                # connect to the left of the current
                if curr.try_left_right(pic, 0):
                    tile.orig = pic
                    curr.left, tile.right = name, curr.name
                    connected = True
                # connect to the right of the current
                elif curr.try_left_right(pic, tile.w - 1):
                    tile.orig = pic
                    curr.right, tile.left = name, curr.name
                    connected = True
                # connect to the top of the current
                elif curr.try_top_bottom(pic, 0):
                    tile.orig = pic
                    curr.top, tile.bottom = name, curr.name
                    connected = True
                # connect to the bottom of the current
                elif curr.try_top_bottom(pic, tile.h - 1):
                    tile.orig = pic
                    curr.bottom, tile.top = name, curr.name
                    connected = True
                if connected and name not in vis:
                    tile_q.append(tile)
                    break


def append_to_photo(photo: Tile, tile: Tile, start_r: int) -> None:
    for r in range(tile.h):
        photo.orig[r + start_r] += tile.orig[r]


''' sea monster pattern
                  #
#    ##    ##    ###
 #  #  #  #  #  #

15 hashtags  in total

.{18}#
#(.{4}##){3}#
.#(..#){5}
'''
def find_monsters(pic: list) -> int:
    i, count, hashtags = 0, 0, 0
    while i <= len(pic) - 3:
        l1, l2, l3 = pic[i], pic[i + 1], pic[i + 2]
        for c in range(len(pic[0]) - 19):
            if re.match(r'.{18}#', l1[c:]) and re.match(r'#(.{4}##){3}#', l2[c:]) and re.match(r'.#(..#){5}', l3[c:]):
                count += 1
        i += 1

    if count:
        for r in pic:
            hashtags += r.count('#')
        hashtags -= count * 15
    return hashtags


with open("input/day20.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    tiles = {}
    i = 0
    while i < len(lines):
        name = lines[i].strip().split(' ')[1][:-1]
        tile = Tile(name)
        i += 1
        while i < len(lines) and lines[i] != '':
            tile.orig.append(lines[i])
            i += 1
        i += 1
        tile.init_rot_flip()
        tiles[name] = tile
    
    # solve the first puzzle
    connect_tiles(name, tiles)

    start = ''
    for name, t in tiles.items():
        if (t.left == None == t.top) or (t.right == None == t.top) or (t.bottom == None and t.right == None) or (t.bottom == None and t.left == None):
            answer1 *= int(name)
        if t.left == None == t.top:  # starting position for the second puzzle
            start = name
        # remove the borders
        del t.orig[t.h - 1]
        del t.orig[0]
        for r in range(t.h - 2):
            t.orig[r] = t.orig[r][1:-1]
        t.h, t.w = t.h - 2, t.w - 2
    
    # solve the second puzzle
    photo = Tile('monster')
    
    go_down = tiles[start]
    i = 0
    while True:
        for _ in range(tiles[start].h):
            photo.orig.append('')
        go_right = go_down
        while True:
            append_to_photo(photo, go_right, tiles[start].h * i)
            if go_right.right == None:
                break
            go_right = tiles[go_right.right]
        if go_down.bottom == None:
            break
        go_down = tiles[go_down.bottom]
        i += 1
    
    photo.h, photo.w = len(photo.orig), len(photo.orig[0])
    photo.init_rot_flip()

    for pic in photo.pics:
        answer2 = max(answer2, find_monsters(pic))


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
