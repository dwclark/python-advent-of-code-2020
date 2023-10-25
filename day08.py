from aoc import non_blank_lines

class Ins:
    def __init__(self, op, num):
        self.op = op
        self.num = num

def load_instructions():
    def parse_instruction(line):
        op, num = line.split(' ')
        return Ins(op, int(num))

    return [parse_instruction(line) for line in non_blank_lines('input/day08.txt')]

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
            
        ins = instructions[ip]
        if(ins.op == 'nop'):
            ip += 1
        elif(ins.op == 'acc'):
            accum += ins.num
            ip += 1
        else:
            ip += ins.num

instructions = load_instructions()

def part_1():
    accum, early = run_machine(instructions)
    return accum

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
            
print("Part 1: ", part_1())
print("Part 2: ", part_2())
