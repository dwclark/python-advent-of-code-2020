from aoc import non_blank_lines, print_assert
from math import prod
from itertools import combinations

n = [ int(s) for s in non_blank_lines('input/day01.txt') ]

def find_answer(count):
    return next((prod(comb) for comb in combinations(n, count) if sum(comb) == 2020))

print_assert("Part 1:", find_answer(2), 956091)
print_assert("Part 2:", find_answer(3), 79734368)

