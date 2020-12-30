import re


answer1, answer2 = 0, 0


def is_valid(info: dict) -> int:
    if int(info['byr']) < 1920 or int(info['byr']) > 2002:
        return 0
    if int(info['iyr']) < 2010 or int(info['iyr']) > 2020:
        return 0
    if int(info['eyr']) < 2020 or int(info['eyr']) > 2030:
        return 0
    if 'in' not in info['hgt'] and 'cm' not in info['hgt']:
        return 0
    if 'in' in info['hgt'] and (int(info['hgt'].split('in')[0]) < 59 or int(info['hgt'].split('in')[0]) > 76):
        return 0
    if 'cm' in info['hgt'] and (int(info['hgt'].split('cm')[0]) < 150 or int(info['hgt'].split('cm')[0]) > 193):
        return 0
    if re.search(r'^#[0-9a-f]{6}$', info['hcl']) is None:
        return 0
    if re.search(r'amb|blu|brn|gry|grn|hzl|oth', info['ecl']) is None:
        return 0
    if re.search(r'^[0-9]{9}$', info['pid']) is None:
        return 0
    return 1


with open('input/day04.in') as f:
    lines = f.readlines()
    info = {}
    for line in lines:
        line = line.strip()
        if line == '':
            if (len(info) == 7 and 'cid' not in info) or len(info) == 8:
                answer1 += 1
                answer2 += is_valid(info)
            info = {}
        else:
            for pair in line.split():
                key_value = pair.split(':')
                info[key_value[0]] = key_value[1]


print('Answer 1: ' + str(answer1))
print('Answer 2: ' + str(answer2))
