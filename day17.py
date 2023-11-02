from aoc import non_blank_lines, print_assert

class Vec(tuple):

    def init_neighbors(zero, accum, *args):
        if len(args) == len(zero):
            if args != zero:
                accum.append(Vec(tuple(args)))
            return accum

        for i in [-1, 0, 1]:
            Vec.init_neighbors(zero, accum, *args, i)

        return accum
    
    neighbor_indices = {}
    
    def __add__(self, rhs):
        return Vec(x + y for x,y in zip(self, rhs))

Vec.neighbor_indices[3] = Vec.init_neighbors((0,0,0), [])
Vec.neighbor_indices[4] = Vec.init_neighbors((0,0,0,0), [])

def initialize_game(dims):
    return {Vec([ x, y ] + ([0] * (dims - 2))):1
            for x, line in enumerate(non_blank_lines('input/day17.txt'))
            for y, s in enumerate(line) if s == '#'}

def game_limits(dims, cubes):
    mins, maxes = {}, {}
    for cube in cubes.keys():
        for i, d in enumerate(cube):
            current_min = mins.get(i, None)
            if current_min is None or d-1 < current_min:
                mins[i] = d-1
                
            current_max = maxes.get(i, None)
            if current_max is None or current_max < d+1:
                maxes[i] = d+1

    return [(mins[i], maxes[i]) for i in range(dims)]

def active_neighbors(dims, cube, cubes):
    return sum([cubes.get(cube + index, 0) for index in Vec.neighbor_indices[dims]])

def check_all_cubes(dims, limits, cubes, new_cubes, *coords):
    if not limits:
        cube = Vec(coords)
        im_active = cubes.get(cube, 0)
        theyre_active = active_neighbors(dims, cube, cubes)
        if ((im_active and theyre_active in range(2,4)) or
            (not im_active and theyre_active == 3)):
            new_cubes[cube] = 1
    else:
        for i in range(limits[0][0], limits[0][1]+1):
            check_all_cubes(dims, limits[1:], cubes, new_cubes, *coords, i)

    return new_cubes
            
def play_game(dims, rounds):
    cubes = initialize_game(dims)
    for r in range(rounds):
        limits = game_limits(dims, cubes)
        cubes = check_all_cubes(dims, limits, cubes, {})
    return len(cubes)

print_assert("Part 1:", play_game(3, 6), 213)
print_assert("Part 2:", play_game(4, 6), 1624)
