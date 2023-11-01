from aoc import non_blank_lines, print_assert
import re

re_contents = re.compile(r"(\d+) ([a-z]+ [a-z]+)")
re_bag_color =  re.compile("^([a-z]+ [a-z]+)")

class Bag:
    def __init__(self, line):
        self.color = re.findall(re_bag_color, line)[0]
        self.contents = { tup[1]:int(tup[0]) for tup in re.findall(re_contents, line) }

colors_to_bags = { b.color: b for b in [Bag(line) for line in non_blank_lines('input/day07.txt')] }

def contains_shiny_gold(color):
    for new_color in colors_to_bags[color].contents.keys():
        if (new_color == 'shiny gold' or contains_shiny_gold(new_color)):
            return True
    return False

def num_sub_bags(bag):
    return sum((count + (count * num_sub_bags(colors_to_bags[color]))) for color, count in bag.contents.items())

def part_1():
    return len([color for color in colors_to_bags.keys() if color != 'shiny gold' and contains_shiny_gold(color)])

print_assert("Part 1:", part_1(), 246)
print_assert("Part 2:", num_sub_bags(colors_to_bags['shiny gold']), 2976)
