import re


answer1, answer2 = 0, 0


def get_valid_msg(start: str, rules: list, visited: dict) -> list:
    if start in visited:
        return visited[start]
    if '"' != start[0]:
        msgs = []  # stores lists of possible messages
        for rule in rules[start]:  # go over rules separated with |
            msg = ['']
            for r in rule.split(' '):  # go over the individual rule numbers
                valid_msgs = get_valid_msg(r, rules, visited)
                visited[r] = valid_msgs
                msg = [m + a for s in valid_msgs for m in msg for a in s]
            msgs.append(msg)
        return msgs
    return [[start[1:-1]]]


# 8:  42 | 42 8         (42+)
# 11: 42 31 | 42 11 31  (42{x}31{x})
# 42+42{x}31{x}
def check_message(msg: list, list_42: list, list_31: list) -> int:
    count = 0
    v_42 = '|'.join(list_42)
    v_31 = '|'.join(list_31)
    for x in range(1, 8):
        m_to_del = []
        for m in msg:
            pat = r'^({})+({}){}({}){}$'.format(v_42, v_42, '{' + str(x) + '}', v_31, '{' + str(x) + '}')
            if re.match(pat, m):
                m_to_del.append(m)
                count += 1
        for m in m_to_del:
            msg.remove(m)
    return count


with open("input/day19.in", "r") as f:
    rules = {}
    msg   = []
    for line in f:
        if line.strip() == '': break
        s_r = line.strip().split(': ')  # split rule
        rules[s_r[0]] = s_r[1].split(' | ')
    
    for line in f:
        msg.append(line.strip())

    # solve the first puzzle
    valid_msg = set()
    [valid_msg.add(v) for v_m in get_valid_msg('0', rules, {}) for v in v_m]

    for m in msg:
        if m in valid_msg:
            answer1 += 1
    
    # solve the second puzzle
    rules['8'] = '42 | 42 8'.split(' | ')
    rules['11'] = '42 31 | 42 11 31'.split(' | ')

    v_42, v_31 = [], []

    # remove duplicates just in case
    [v_42.append(m) for ms in get_valid_msg('42', rules, {}) for m in ms if m not in v_42]
    [v_31.append(m) for ms in get_valid_msg('31', rules, {}) for m in ms if m not in v_31]
    
    answer2 = check_message(msg, v_42, v_31)


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
