from aoc import blank_line_grouped, print_assert
from functools import reduce

groups = blank_line_grouped('input/day06.txt')

def solve(reducer):
    return sum([len(s) for s in [reduce(reducer, group) for group in groups]])

print_assert("Part 1:", solve(lambda one, two: set(one) | set(two)), 7283)
print_assert("Part 2:", solve(lambda one, two: set(one) & set(two)), 3520)
