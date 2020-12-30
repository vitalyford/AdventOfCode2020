answer1, answer2 = 0, 0


def prec(c: str) -> int:
    return 2 if c == '+' else 1


def postfix(line: str, apply_prec: bool) -> list:
    out = []
    s   = []  # stack to handle operators
    for c in line:
        if c.isspace(): continue
        if c.isdigit():
            out.append(c)
        elif c == '(':
            s.append(c)
        elif c == ')':
            while len(s) > 0 and s[-1] != '(':
                out.append(s.pop())
            s.pop()  # pop '('
        else:  # process an operator
            while len(s) > 0 and s[-1] != '(' and (not apply_prec or prec(s[-1]) >= prec(c)):
                out.append(s.pop())
            s.append(c)
    while len(s) > 0:
        out.append(s.pop())
    return out


def eval_postfix(arr: list) -> int:
    s = []  # stack to keep operands
    for a in arr:
        if a.isdigit():
            s.append(int(a))
        else:
            if a == '+':
                s.append(s.pop() + s.pop())
            else:
                s.append(s.pop() * s.pop())
    return s[0]


with open("input/day18.in", "r") as f:
    for line in f.readlines():
        answer1 += eval_postfix(postfix(line.strip(), False))
        answer2 += eval_postfix(postfix(line.strip(), True))


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
