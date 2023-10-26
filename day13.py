from aoc import non_blank_lines

data = non_blank_lines('input/day13.txt')
earliest = int(data[0])
timestamps = data[1].split(',')

def wait_time(val, target):
    to_add = 0 if target % val == 0 else 1
    divisor = target // val
    return (val * (divisor + to_add)) - target

def remainder_list(timestamps):
    return [(int(val) - i) % int(val) if val != 'x' else 0 for i, val in enumerate(timestamps)]
        
def part_1():
    filtered = list(map(int, filter(lambda v: v != 'x', timestamps)))
    wait_times = { val: wait_time(val, earliest) for val in filtered }
    the_min = min(wait_times.items(), key=(lambda i: i[1]))
    return the_min[0] * the_min[1]

def part_2():
    result = 0
    increment = 1
    for val, remainder in zip(timestamps, remainder_list(timestamps)):
        if val == 'x':
            continue
        
        num = int(val)
        while not result % num == remainder:
            result += increment
        increment *= num

    return result

print("Part 1:", part_1())
print("Part 2:", part_2())
