answer1 = 0


def get_enc_key(sub_num: int, loop_num: int) -> int:
    val = 1
    for _ in range(loop_num):
        val *= sub_num
        val = val % 20201227
    return val


def find_loop(pub: int) -> int:
    val, i, sub_num = 1, 1, 7
    while True:
        val *= sub_num
        val = val % 20201227
        if val == pub:
            break
        i += 1
    return i


with open("input/day25.in", "r") as f:
    card_pub = int(f.readline())
    door_pub = int(f.readline())
    
    card_loop = find_loop(card_pub)
    door_loop = find_loop(door_pub)
    
    answer1 = get_enc_key(card_pub, door_loop)


print('Answer 1: ' + str(answer1))
print('Answer 2: free star at the bottom of the pouch!')
