from aoc import non_blank_lines

def row(s):
    return int(s[0:7].replace('F', '0').replace('B', '1'), base=2)

def column(s):
    return int(s[7:].replace('R', '1').replace('L', '0'), base=2)

def seat_id(s):
    return (row(s) * 8) + column(s)

all_ids = sorted(list(map(seat_id, non_blank_lines("input/day05.txt"))))

def part_2():
    for idx in range(1, len(all_ids) - 1):
        if all_ids[idx] + 1 != all_ids[idx+1]:
            return (all_ids[idx] + 1)

print("Part 1: ", max(all_ids))
print("Part 2: ", part_2())
