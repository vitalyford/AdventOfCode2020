answer1, answer2 = 0, 0


def no_occupied_adjacent(seats: list, row: int, col: int) -> bool:
    for r in range(max(0, row - 1), min(row + 2, len(seats))):
        for c in range(max(0, col - 1), min(col + 2, len(seats[0]))):
            if seats[r][c] == '#':
                return False
    return True


def four_or_more_occupied(seats: list, row: int, col: int) -> bool:
    occupied = 0
    for r in range(max(0, row - 1), min(row + 2, len(seats))):
        for c in range(max(0, col - 1), min(col + 2, len(seats[0]))):
            if seats[r][c] == '#':
                occupied += 1
    return occupied >= 5


def occupied_visible(seats: list, row: int, col: int) -> int:
    occupied = 0

    # go up
    r = row - 1
    while r >= 0:
        if seats[r][col] == '#':
            occupied += 1
            break
        elif seats[r][col] == 'L':
            break
        r -= 1
    
    # go down
    r = row + 1
    while r < len(seats):
        if seats[r][col] == '#':
            occupied += 1
            break
        elif seats[r][col] == 'L':
            break
        r += 1
    
    # go left
    c = col - 1
    while c >= 0:
        if seats[row][c] == '#':
            occupied += 1
            break
        elif seats[row][c] == 'L':
            break
        c -= 1
    
    # go right
    c = col + 1
    while c < len(seats[0]):
        if seats[row][c] == '#':
            occupied += 1
            break
        elif seats[row][c] == 'L':
            break
        c += 1

    # go up-left
    c = col - 1
    r = row - 1
    while r >= 0 and c >= 0:
        if seats[r][c] == '#':
            occupied += 1
            break
        elif seats[r][c] == 'L':
            break
        c -= 1
        r -= 1
    
    # go up-right
    c = col + 1
    r = row - 1
    while r >= 0 and c < len(seats[0]):
        if seats[r][c] == '#':
            occupied += 1
            break
        elif seats[r][c] == 'L':
            break
        c += 1
        r -= 1
    
    # go down-right
    c = col + 1
    r = row + 1
    while r < len(seats) and c < len(seats[0]):
        if seats[r][c] == '#':
            occupied += 1
            break
        elif seats[r][c] == 'L':
            break
        c += 1
        r += 1
    
    # go down-left
    c = col - 1
    r = row + 1
    while r < len(seats) and c >= 0:
        if seats[r][c] == '#':
            occupied += 1
            break
        elif seats[r][c] == 'L':
            break
        c -= 1
        r += 1
    
    return occupied


with open("input/day11.in", "r") as f:
    lines = f.readlines()

    # solve the first puzzle
    seats = [line.strip() for line in lines]
    
    while True:
        no_changes = True
        new_seats = []

        for row in range(len(seats)):
            line = ''
            for col in range(len(seats[0])):
                if seats[row][col] == 'L' and no_occupied_adjacent(seats, row, col):
                    line += '#'
                    no_changes = False
                elif seats[row][col] == '#' and four_or_more_occupied(seats, row, col):
                    line += 'L'
                    no_changes = False
                else:
                    line += seats[row][col]
            new_seats.append(line)
        
        seats = new_seats

        if no_changes:
            break
    
    answer1 = sum([line.count('#') for line in seats])

    # solve the second puzzle
    seats = [line.strip() for line in lines]

    while True:
        no_changes = True
        new_seats = []

        for row in range(len(seats)):
            line = ''
            for col in range(len(seats[0])):
                if seats[row][col] == 'L' and occupied_visible(seats, row, col) == 0:
                    line += '#'
                    no_changes = False
                elif seats[row][col] == '#' and occupied_visible(seats, row, col) >= 5:
                    line += 'L'
                    no_changes = False
                else:
                    line += seats[row][col]
            new_seats.append(line)
        
        seats = new_seats
        
        if no_changes:
            break
    for s in seats:
        print(s)
    answer2 = sum([line.count('#') for line in seats])


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
