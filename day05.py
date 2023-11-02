from aoc import non_blank_lines, print_assert

def load_all():
    row = lambda s: int(s[0:7].replace('F', '0').replace('B', '1'), base=2)
    column = lambda s: int(s[7:].replace('R', '1').replace('L', '0'), base=2)
    seat_id = lambda s: (row(s) * 8) + column(s)
    return sorted([seat_id(line) for line in non_blank_lines("input/day05.txt")])

all_ids = load_all()
print_assert("Part 1:", all_ids[-1], 816)
print_assert("Part 2:", next((f + 1 for f,s in zip(all_ids[1:], all_ids[2:]) if not f+1 == s)), 539)
