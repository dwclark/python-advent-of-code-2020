from aoc import single_int_line, print_assert
import functools
from collections import Counter

def load_all():
    adapters = sorted(single_int_line('input/day10.txt'))
    return tuple([0, *adapters, adapters[-1] + 3])

def part_1(a):
    diffs = Counter((s-f for f,s in zip(a, a[1:])))
    return diffs[1] * diffs[3]

def part_2(my_list):
    @functools.cache
    def try_next(prev, lst):
        rest = lst[1:]

        if lst[0] - prev > 3:
            return 0
        elif not rest:
            return 1
        else:
            return try_next(prev, rest) + try_next(lst[0], rest)

    return try_next(my_list[0], my_list[1:])

adapters = load_all()
print_assert("Part 1:", part_1(adapters), 2760)
print_assert("Part 2:", part_2(adapters), 13816758796288)
