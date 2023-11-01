from aoc import non_blank_lines, print_assert

class Ins:
    def __init__(self, line):
        a = line.split(' ')
        self.op, self.num = a[0], int(a[1])

def run_machine(instructions):
    ip = 0
    accum = 0
    seen = set([])

    while True:
        if(ip >= len(instructions)):
            return (accum, False)
        elif(ip in seen):
            return (accum, True)
        else:
            seen.add(ip)
            
        match instructions[ip]:
            case Ins(op='nop', num=n):
                ip += 1
            case Ins(op='acc', num=n):
                accum += n
                ip += 1
            case Ins(op=_, num=n):
                ip += n

instructions = [Ins(line) for line in non_blank_lines('input/day08.txt')]

def part_2():
    for ins in instructions:
        original = ins.op
        if original == 'nop':
            ins.op = 'jmp'
        elif original == 'jmp':
            ins.op = 'nop'
        else:
            continue
        
        accum, early = run_machine(instructions)
        if not early:
            return accum
        else:
            ins.op = original
            
print_assert("Part 1:", run_machine(instructions)[0], 1782)
print_assert("Part 2:", part_2(), 797)
