from aoc import blank_line_delimited, print_assert
import re

def load_data():
    ret = []
    for line in blank_line_delimited('input/day04.txt'):
        ret.append({ a[0]:a[1] for a in (block.split(':') for block in line.split(' ')) })
    return ret

re_year = re.compile(r"^\d{4}$")
re_hgt = re.compile(r"^(\d{3})(cm)|(\d{2})(in)$")
re_hcl = re.compile(r"^#[0-9a-f]{6}$")
re_ecl = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
re_pid = re.compile(r"^\d{9}$")

def byr(s):
    return re_year.match(s) and (1920 <= int(s) <= 2002)

def iyr(s):
    return re_year.match(s) and (2010 <= int(s) <= 2020)

def eyr(s):
    return re_year.match(s) and (2020 <= int(s) <= 2030)

def hgt(s):
    mat = re_hgt.match(s)
    return mat and ((mat.group(2) == 'cm' and (150 <= int(mat.group(1)) <= 193)) or
                    (mat.group(4) == 'in' and (59 <= int(mat.group(3)) <= 76)))

def valid_keys(passport):
    for field in [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]:
        if not field in passport:
            return False
    return True

def valid_fields(p):
    return (byr(p['byr']) and iyr(p['iyr']) and eyr(p['eyr']) and
            hgt(p['hgt']) and re_hcl.match(p['hcl']) and
            re_ecl.match(p['ecl']) and re_pid.match(p['pid']))

part_1_valid = [p for p in load_data() if valid_keys(p)]
print_assert("Part 1:", len(part_1_valid), 235)
part_2_valid = [p for p in part_1_valid if valid_fields(p)]
print_assert("Part 2:", len(part_2_valid), 194)
