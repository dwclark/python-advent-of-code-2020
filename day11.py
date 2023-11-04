from aoc import non_blank_lines, print_assert
from copy import deepcopy

class Ferry:
    neighbor_indexes = ((-1,-1), (-1, 0), (-1, 1),
                        (0, -1),          (0, 1),
                        (1, -1), (1, 0),  (1, 1))
    
    def __init__(self, grid):
        if type(grid[0]) is str:
            self.grid = [ list(row) for row in grid ]
        else:
            self.grid = grid

    def __deepcopy__(self, memo):
        return type(self)(deepcopy(self.grid, memo))

    def __str__(self):
        return '\n'.join([ ''.join(row) for row in self.grid ])

    def __eq__(self, other):
        return self.grid == other.grid

    def __getitem__(self, key):
        return self.grid[key[0]][key[1]]

    def __setitem__(self, key, value):
        self.grid[key[0]][key[1]] = value

    def in_grid(self, rc):
        return (0 <= rc[0] < len(self.grid)) and (0 <= rc[1] < len(self.grid[0]))

    def is_floor(self, rc):
        return 1 if self[rc] == '.' else 0

    def is_empty(self, rc):
        return 1 if self[rc] == 'L' else 0

    def is_occupied(self, rc):
        return 1 if self[rc] == '#' else 0

    @staticmethod
    def _add(one, two):
        return (one[0] + two[0], one[1] + two[1])
    
    def immediate_neighbors(self, rc):
        for index in Ferry.neighbor_indexes:
            new_rc = Ferry._add(rc, index)
            if self.in_grid(new_rc) and not self.is_floor(new_rc):
                yield new_rc

    def every_seat(self):
        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[0])):
                rc = (row, col)
                if not self.is_floor(rc):
                    yield rc

    def next_grid(self):
        new_ferry = deepcopy(self)
        for seat in self.every_seat():
            occupied = 0
            for neighbor in self.immediate_neighbors(seat):
                occupied += self.is_occupied(neighbor)
            if self.is_empty(seat) and occupied == 0:
                new_ferry[seat] = '#'
            elif self.is_occupied(seat) and occupied >= 4:
                new_ferry[seat] = 'L'
        return new_ferry

class Ferry2(Ferry):

    def next_grid(self):
        new_ferry = deepcopy(self)
        for seat in self.every_seat():
            occupied = 0
            for index in Ferry.neighbor_indexes:
                next_rc = Ferry._add(seat, index)
                while self.in_grid(next_rc):
                    if self.is_occupied(next_rc):
                        occupied += 1
                        break
                    elif self.is_empty(next_rc):
                        break
                    else:
                        next_rc = Ferry._add(next_rc, index)
                        
            if self.is_empty(seat) and occupied == 0:
                new_ferry[seat] = '#'
            elif self.is_occupied(seat) and occupied >= 5:
                new_ferry[seat] = 'L'
                
        return new_ferry
                    

def solve(con):
    prev = con(non_blank_lines('input/day11.txt'))
    current = prev.next_grid()
    while prev != current:
        prev = current
        current = prev.next_grid()

    return len([s for s in current.every_seat() if current.is_occupied(s)])

print_assert("Part 1:", solve(Ferry), 2093)
print_assert("Part 2:", solve(Ferry2), 1862)
