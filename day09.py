answer1, answer2 = 0, 0


def find_contiguous(lines: list, invalid_num: int) -> int:
    start, end = 0, 1
    while True:
        s = sum(lines[start:end])
        if s == invalid_num:
            return min(lines[start:end]) + max(lines[start:end])
        elif s < invalid_num:
            end += 1
        elif s > invalid_num:
            start += 1
    return -1


with open("input/day09.in", "r") as f:
    lines = [int(line) for line in f.readlines()]

    preamble   = 25
    start, end = 0, preamble

    # solve the first puzzle
    while True:
        window = set()
        is_valid = False
        for num in lines[start:end]:
            if lines[end] - num in window:
                is_valid = True
                break
            window.add(num)
        if not is_valid:
            answer1 = lines[end]
            break
        start += 1
        end   += 1

    # solve the second puzzle
    answer2 = find_contiguous(lines, answer1)


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
