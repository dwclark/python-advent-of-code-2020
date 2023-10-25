from aoc import non_blank_lines
from collections import namedtuple

Pwd = namedtuple('Pwd', 'num1 num2 look_for pwd')

def as_tuple(line):
    r, c, s = line.split(' ')
    low, high = r.split('-')
    return Pwd(int(low), int(high), c.replace(':',''), s)

def all_passwords():
    return [as_tuple(line) for line in non_blank_lines('input/day02.txt')]

def part_1():
    def is_valid(info):
        return info.num1 <= info.pwd.count(info.look_for) <= info.num2
    
    return [is_valid(password) for password in all_passwords()].count(True)

def part_2():
    def is_valid(info):
        return (info.pwd[info.num1-1] == info.look_for) ^ (info.pwd[info.num2-1] == info.look_for)
    
    return [is_valid(password) for password in all_passwords()].count(True)

print("Part 1: ", part_1())
print("Part 2: ", part_2())
