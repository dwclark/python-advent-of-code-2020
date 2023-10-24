from aoc import non_blank_lines
from collections import namedtuple

Pwd = namedtuple('Pwd', 'num1 num2 look_for pwd')

def as_tuple(line):
    r, c, s = line.split(' ')
    low, high = r.split('-')
    return Pwd(int(low), int(high), c.replace(':',''), s)

def all_passwords():
    return list(map(as_tuple, non_blank_lines('input/day02.txt')))

def part_1():
    def is_valid(info):
        return info.num1 <= info.pwd.count(info.look_for) <= info.num2
    
    return list(map(is_valid, all_passwords())).count(True)

def part_2():
    def is_valid(info):
        return (info.pwd[info.num1-1] == info.look_for) ^ (info.pwd[info.num2-1] == info.look_for)
    
    return list(map(is_valid, all_passwords())).count(True)
