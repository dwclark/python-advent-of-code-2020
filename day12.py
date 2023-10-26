from aoc import non_blank_lines
from collections import deque

class Ship:
    directionsMap = { 'E': 0, 'S': 1, 'W': 2, 'N': 3 }

    def toDirections(dirMap):
        ret = [0,0,0,0]
        for k,v in dirMap.items():
            ret[Ship.directionsMap[k]] = v
        return ret
    
    def __init__(self, initialMap):
        self.x = 0
        self.y = 0
        self.directions = deque(Ship.toDirections(initialMap))

    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def rotate(self, direction, degrees):
        self.directions.rotate((degrees // 90) * (1 if direction == 'R' else -1))

    def move(self, dirs, by):
        self.x += (dirs[0] * by) - (dirs[2] * by)
        self.y += (dirs[3] * by) - (dirs[1] * by)

    def compass_action(self, move):
        dirs = [0,0,0,0]
        dirs[Ship.directionsMap[move[0]]] = 1
        self.move(dirs, move[1])
        
    def action(self, move):
        if move[0] in ['N','S','E','W']:
            self.compass_action(move)
        elif move[0] == 'F':
            self.move(list(self.directions), move[1])
        else:
            self.rotate(move[0], move[1])

    def actions(self, all):
        for a in all:
            self.action(a)

        return self

class Ship2(Ship):
    def compass_action(self, move):
        self.directions[Ship.directionsMap[move[0]]] += move[1]

def load():
    return [ (line[0], int(line[1:])) for line in non_blank_lines('input/day12.txt') ]

my_actions = load()
print("Part 1:", Ship({'E': 1}).actions(my_actions).manhattan())
print("Part 2:", Ship2({'E': 10, 'N': 1}).actions(my_actions).manhattan())

        
