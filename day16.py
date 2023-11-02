from aoc import non_blank_lines, print_assert
import re
import functools
from math import prod

class Rule: #for caching to work correctly
    def __init__(self, name, r1, r2):
        self.name = name
        self.r1 = r1
        self.r2 = r2

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def valid(self, val):
        return (val in self.r1) or (val in self.r2)
    
def parse_ticket(line):
    return [int(s) for s in line.split(',')]

pattern = re.compile(r"^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$")

def parse_rule(line):
    m = pattern.match(line)
    name = m.group(1)
    r1 = range(int(m.group(2)), int(m.group(3)) + 1)
    r2 = range(int(m.group(4)), int(m.group(5)) + 1)
    return Rule(name, r1, r2)
    
def load():
    mode = 0
    rules = []
    my_ticket = None
    nearby_tickets = []
    
    for line in non_blank_lines('input/day16.txt'):
        if line == 'your ticket:':
            mode = 1
            continue
        elif line == 'nearby tickets:':
            mode = 2
            continue

        if mode == 0:
            rules.append(parse_rule(line))
        elif mode == 1:
            my_ticket = parse_ticket(line)
        else:
            nearby_tickets.append(parse_ticket(line))

    return (rules, my_ticket, nearby_tickets)

def is_valid(val):
    return any(map(lambda rule: rule.valid(val), rules))

def only_valid(tickets):
    ret = []
    
    for ticket in tickets:
        valid = True
        for val in ticket:
            if not is_valid(val):
                valid = False
                break
        if valid:
            ret.append(ticket)
            
    return ret

rules, my_ticket, nearby_tickets = load()
valid = only_valid(nearby_tickets)

@functools.cache
def valid_at_index(rule, idx):
    for ticket in valid:
        if not rule.valid(ticket[idx]):
            return False
        
    return True

def satisfy(satisfied, unsatisfied):
    if len(satisfied) == len(rules):
        return satisfied
    
    index = len(satisfied)
    for i, rule in enumerate(unsatisfied):
        if valid_at_index(rule, index):
            satisfied.append(rule)
            satisfy(satisfied, unsatisfied[0:i] + unsatisfied[(i+1):])
            if len(satisfied) == len(rules):
                return satisfied
            else:
                satisfied.pop()

    return []
    
def part_1():
    return sum((val for ticket in nearby_tickets for val in ticket if not is_valid(val)))

def part_2():
    satisfied = satisfy([], rules)
    return prod((val for rule, val in zip(satisfied, my_ticket) if rule.name.startswith('departure')))

print_assert("Part 1:", part_1(), 23036)
print_assert("Part 2:", part_2(), 1909224687553)
