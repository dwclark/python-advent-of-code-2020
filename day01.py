from aoc import non_blank_lines, print_assert
import math

n = [ int(s) for s in non_blank_lines('input/day01.txt') ]

gen_1 = ((n[outer], n[inner]) for outer in range(0, len(n)-1) for inner in range(1, len(n))
         if n[outer] + n[inner] == 2020)

gen_2 = ((n[outer], n[middle], n[inner])
         for outer in range(0, len(n)-2)
         for middle in range(1, len(n)-1)
         for inner in range(2, len(n))
         if n[outer] + n[middle] + n[inner] == 2020)

print_assert("Part 1:", math.prod(next(gen_1)), 956091)
print_assert("Part 2:", math.prod(next(gen_2)), 79734368)

