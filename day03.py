from aoc import non_blank_lines

grid = non_blank_lines('input/day03.txt')
width = len(grid[0])

def next_x(cur, x_by):
    tmp = cur + x_by
    if tmp < width:
        return tmp
    else:
        return tmp - width

def traverse_grid(x_by, y_by):
    tot = 0
    x = -x_by
    
    for y in range(0, len(grid), y_by):
        x = next_x(x, x_by)
        if grid[y][x] == '#':
            tot += 1
            
    return tot

print("Part 1: ", traverse_grid(3, 1))
print("Part 2: ", (traverse_grid(1, 1) * traverse_grid(3, 1) * traverse_grid(5, 1) *
                   traverse_grid(7, 1) * traverse_grid(1, 2)))
