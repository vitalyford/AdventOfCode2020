answer1, answer2 = 0, 0


def dec_to_bin(num: int) -> list:
    return [] if num == 0 else dec_to_bin(num // 2) + [num % 2]


def bin_to_dec(num: list) -> int:
    sum = 0
    for i, n in enumerate(num):
        if n == 1:
            sum += 1 << (36 - i - 1)
    return sum


def apply_mask(mask: list, num: list) -> list:
    for i, b in enumerate(mask[::-1]):
        if i >= len(num):
            num = [int(b) if b != 'X' else 0] + num
        elif b == '0' or b == '1':
            num[-i - 1] = int(b)
    return num


def gen_addrs(addr: list, start_index: int, addrs: list) -> None:
    is_floating = False

    for i in range(start_index, len(addr)):
        if addr[i] == 2:  # floating bit
            addr[i] = 0
            gen_addrs(addr[:], i + 1, addrs)
            addr[i] = 1
            gen_addrs(addr, i + 1, addrs)
            is_floating = True

    if not is_floating:
        addrs.append(bin_to_dec(addr))


def apply_mask_v2(mask: list, addr: list):
    for i, b in enumerate(mask[::-1]):
        if i >= len(addr):
            if b == '1':
                addr = [1] + addr
            elif b == 'X':
                addr = [2] + addr
            else:
                addr = [0] + addr
        elif b == '1':
            addr[-i - 1] = 1
        elif b == 'X':
            addr[-i - 1] = 2  # floating bit
    
    addrs = []
    gen_addrs(addr, 0, addrs)

    return addrs


with open("input/day14.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    # solve the first puzzle
    vals = {}
    i = 0
    while i < len(lines):
        mask = lines[i].strip().split(' = ')[1]
        
        i += 1
        mem_input = []
        while i < len(lines) and lines[i][1] == 'e':  # while looking at mem
            mem_input.append(lines[i])
            i += 1
        
        for mem in mem_input:
            pos = int(mem.split('[')[1].split(']')[0])
            val = int(mem.split(' = ')[1])
            res = apply_mask(mask, dec_to_bin(val))
            vals[pos] = bin_to_dec(res)
    
    answer1 = sum(vals.values())

    # solve the second puzzle
    vals = {}
    i = 0
    while i < len(lines):
        mask = lines[i].strip().split(' = ')[1]
        
        i += 1
        mem_input = []
        while i < len(lines) and lines[i][1] == 'e':  # while looking at mem
            mem_input.append(lines[i])
            i += 1
        
        for mem in mem_input:
            pos = int(mem.split('[')[1].split(']')[0])
            val = int(mem.split(' = ')[1])

            addrs = apply_mask_v2(mask, dec_to_bin(pos))
            for addr in addrs:
                vals[addr] = val
    
    answer2 = sum(vals.values())
    

print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
