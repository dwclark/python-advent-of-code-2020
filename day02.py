from aoc import non_blank_lines, print_assert

class Pwd:
    def __init__(self, line):
        r, c, self.pwd = line.split(' ')
        self.look_for = c.replace(':', '')
        self.num1, self.num2 = (int(v) for v in r.split('-'))
        
all_passwords = [Pwd(line) for line in non_blank_lines('input/day02.txt')]

def count(is_valid):
    return len([password for password in all_passwords if is_valid(password)])

print_assert("Part 1:", count(lambda p: p.num1 <= p.pwd.count(p.look_for) <= p.num2), 469)
print_assert("Part 2:", count(lambda p: (p.pwd[p.num1-1] == p.look_for) ^ (p.pwd[p.num2-1] == p.look_for)), 267)
