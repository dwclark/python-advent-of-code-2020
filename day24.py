from aoc import non_blank_lines, print_assert
from enum import Enum
import re

class Direction(Enum):
    w = (-1,0)
    nw = (0,-1)
    ne = (1,-1)
    e = (1,0)
    se = (0,1)
    sw = (-1,1)
    
    @staticmethod
    def find(letter):
        match letter:
            case 'w':
                return Direction.w
            case 'nw':
                return Direction.nw
            case 'ne':
                return Direction.ne
            case 'e':
                return Direction.e
            case 'se':
                return Direction.se
            case 'sw':
                return Direction.sw

class Tile:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __eq__(self, other):
        return self.v1 == other.v1 and self.v2 == other.v2

    def __hash__(self):
        return 31 * self.v1 + self.v2

    def __repr__(self):
        return f"Tile({self.v1}, {self.v2})"

    def walk_to(self, steps):
        for step in steps:
            self.v1 += step.value[0]
            self.v2 += step.value[1]
        return self

    def neighbors(self):
        return (Tile(self.v1 + d.value[0], self.v2 + d.value[1]) for d in Direction)
        
def load():
    pattern = re.compile('e|w|ne|nw|se|sw')
    line_to_walk = lambda s: [Direction.find(sub) for sub in pattern.findall(s)]
    return [line_to_walk(line) for line in non_blank_lines('input/day24.txt')]

def do_walks():
    floor = set()
    for steps in load():
        tile = Tile(0,0).walk_to(steps)
        if tile in floor:
            floor.remove(tile)
        else:
            floor.add(tile)
    return floor

def do_flips(times):
    floor = do_walks()

    for time in range(times):
        to_remove = set()
        to_add = set()
        for tile in floor:
            white_neighbors = set()
            black_neighbors = set()
            for n in tile.neighbors():
                if n in floor:
                    black_neighbors.add(n)
                else:
                    white_neighbors.add(n)
            if len(black_neighbors) == 0 or len(black_neighbors) > 2:
                to_remove.add(tile)
                
            for white_tile in white_neighbors:
                if sum((1 for n in white_tile.neighbors() if n in floor)) == 2:
                    to_add.add(white_tile)
                    
        floor.difference_update(to_remove)
        floor.update(to_add)

    return floor

print_assert("Part 1:", len(do_walks()), 495)
print_assert("Part 2:", len(do_flips(100)), 4012)
