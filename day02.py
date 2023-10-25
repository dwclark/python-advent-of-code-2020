from aoc import non_blank_lines
from collections import namedtuple

Pwd = namedtuple('Pwd', 'num1 num2 look_for pwd')

def all_passwords():
    def as_tuple(line):
        r, c, s = line.split(' ')
        low, high = r.split('-')
        return Pwd(int(low), int(high), c.replace(':',''), s)

    return [as_tuple(line) for line in non_blank_lines('input/day02.txt')]

def count(is_valid):
    return [is_valid(password) for password in all_passwords()].count(True)

print("Part 1: ", count(lambda info: info.num1 <= info.pwd.count(info.look_for) <= info.num2))
print("Part 2: ", count(lambda info: (info.pwd[info.num1-1] == info.look_for) ^ (info.pwd[info.num2-1] == info.look_for)))
