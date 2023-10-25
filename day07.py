from aoc import non_blank_lines
from collections import namedtuple
import re

Bag = namedtuple('Bag', 'color contents')

def load_all():
    re_contents = re.compile(r"^(\d+) ([a-z]+ [a-z]+)$")
    
    def parse_bag(line):
        s = line.replace('bags', '').replace('bag', '').replace('.', '')
        bag_color, contents = s.split(' contain ')
        bag_color = bag_color.strip()
        m = {}

        for content in list(map(lambda c: c.strip(), contents.split(','))):
            mat = re_contents.match(content)
            if mat:
                m[mat.group(2)] = int(mat.group(1))
                
        return Bag(bag_color, m)

    bags = list(map(parse_bag, non_blank_lines('input/day07.txt')))
    return { b.color: b for b in bags }

colors_to_bags = load_all()

def contains_shiny_gold(color):
    for new_color in colors_to_bags[color].contents.keys():
        if (new_color == 'shiny gold' or contains_shiny_gold(new_color)):
            return True
    return False

def num_sub_bags(bag):
    tot = 0
    for color, count in bag.contents.items():
        tot += (count + (count * num_sub_bags(colors_to_bags[color])))
    return tot

def part_1():
    return len(list(filter(lambda color: color != 'shiny gold' and contains_shiny_gold(color),
                           colors_to_bags.keys())))
        
def part_2():
    return num_sub_bags(colors_to_bags['shiny gold'])

print("Part 1: ", part_1())
print("Part 2: ", part_2())
    




