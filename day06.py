from aoc import blank_line_grouped
from functools import reduce

groups = blank_line_grouped('input/day06.txt')

def solve(reducer):
    return sum([len(s) for s in [reduce(reducer, group) for group in groups]])

print("Part 1: ", solve(lambda one, two: set(one) | set(two)))
print("Part 2: ", solve(lambda one, two: set(one) & set(two)))
