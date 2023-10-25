from aoc import single_int_line
import functools

def load_all():
    adapters = single_int_line('input/day10.txt')
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return tuple(adapters)

def part_1(adapters):
    diffs = {}
    for index in range(0, len(adapters) - 1):
        diff = adapters[index+1] - adapters[index]
        diffs[diff] = diffs.get(diff, 0) + 1
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
print("Part 1:", part_1(adapters))
print("Part 2:", part_2(adapters))
