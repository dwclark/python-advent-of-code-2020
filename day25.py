from aoc import print_assert

public_keys = (14222596, 4057428)
divisor = 20201227
subject_number = 7

def transform(s):
    val = 1
    while True:
        val = (val * s) % divisor
        yield val

def part_1():
    loop_size = next(i for i, val in enumerate(transform(subject_number)) if val == public_keys[0])
    return next(val for i, val in enumerate(transform(public_keys[1])) if i == loop_size)

print_assert("Part 1:", part_1(), 3286137)
