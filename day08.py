answer1, answer2 = 0, 0


def calc_acc(lines: list) -> (int, int):
    acc = 0
    i = 0
    seen_ops = set()

    while i + 1 != len(lines):
        i += 1

        if i in seen_ops:
            return acc, i

        seen_ops.add(i)

        op  = lines[i].split()[0]
        val = lines[i].split()[1]

        if op == 'acc':
            if val[0] == '+':
                acc += int(val[1:])
            else:
                acc -= int(val[1:])
        elif op == 'jmp':
            if val[0] == '+':
                i += int(val[1:]) - 1
            else:
                i -= int(val[1:]) + 1

    return acc, i


with open("input/day08.in", "r") as f:
    lines = f.readlines()
    
    answer1, _ = calc_acc(lines)

    for k, line in enumerate(lines):
        temp_lines = lines[:]

        if 'nop' in line:
            temp_lines[k] = line.replace('nop', 'jmp')
        elif 'jmp' in line:
            temp_lines[k] = line.replace('jmp', 'nop')

        acc, i = calc_acc(temp_lines)

        if i + 1 == len(lines):
            answer2 = acc
            break


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
