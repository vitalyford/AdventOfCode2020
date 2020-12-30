answer1, answer2 = 0, 0


def calc(lines: list, right: int, down: int) -> int:
    row, col, answer = 0, 0, 0
    while row < len(lines):
        if lines[row][col] == '#':
            answer += 1
        row += down
        col = (col + right) % len(lines[0])
    return answer
    

with open('input/day03.in') as f:
    lines = [line.strip() for line in f.readlines()]
    answer1 = calc(lines, 3, 1)
    answer2 = calc(lines, 1, 1) * calc(lines, 5, 1) * calc(lines, 7, 1) * calc(lines, 1, 2) * answer1


print('Asnwer 1: ' + str(answer1))
print('Asnwer 2: ' + str(answer2))
