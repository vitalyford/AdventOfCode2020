from functools import reduce


answer1, answer2 = 0, 0


def verified(start: int, buses: list) -> bool:
    for bus, i in buses:
        if (start + i) % bus != 0:
            return False
    return True


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


# solve the first puzzle
with open("input/day13.in", "r") as f:
    depart = int(f.readline())
    buses = [int(bus) for bus in f.readline().split(',') if bus != 'x']
    
    my_bus = -1
    min     = 1 << 31
    for bus in buses:
        delta = depart // bus * bus + bus - depart
        if delta < min:
            my_bus = bus
            min    = delta
    
    answer1 = my_bus * (0 if depart % my_bus == 0 else (depart // my_bus * my_bus + my_bus - depart))


# solve the second puzzle
with open("input/day13.in", "r") as f:
    f.readline()
    buses = [(int(bus), i) for i, bus in enumerate(f.readline().split(',')) if bus != 'x']

    # using Chinese remainder theorem
    # formula taken from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    answer2 = chinese_remainder([bus[0] for bus in buses], [bus[0] - bus[1] for bus in buses])


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
