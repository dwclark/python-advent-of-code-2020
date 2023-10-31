from aoc import non_blank_lines
from functools import reduce, partial
import copy

class Food:
    def __init__(self, line):
        groups = line.split('(contains')
        self.ingredients = set(groups[0].strip().split(' '))
        self.allergens = set(groups[1].replace(')', '').strip().split(', '))

def initial_possible(foods):
    table = {}
    for food in foods:
        for allergen in food.allergens:
            if allergen in table.keys():
                table[allergen] = table[allergen] & food.ingredients
            else:
                table[allergen] = food.ingredients
    return table

def for_sure(table):
    for_sure = copy.deepcopy(table)

    def find_matching(fun):
        return dict(filter(fun , possible.items()))

    def find_singles():
        return find_matching(lambda item: len(item[1]) == 1) 

    def find_multiples():
        return find_matching(lambda item: len(item[1]) > 1)
    
    singles = find_singles()
    multiples = find_multiples()
    
    while len(table) != len(singles):
        for allergen, ingredients in singles.items():
            ingredient = list(ingredients)[0]
            for mult_allergen, mult_ingredients in multiples.items():
                mult_ingredients.discard(ingredient)
        singles = find_singles()
        multiples = find_multiples()

    return for_sure

def foods_possible_impossible():
    foods = [Food(line) for line in non_blank_lines('input/day21.txt')]
    sure = for_sure(initial_possible(foods))
    all_ingredients = reduce(lambda s1, s2: s1 | s2, [food.ingredients for food in foods], set())
    impossible = all_ingredients - reduce(lambda s1, s2: s1 | s2, sure.values(), set())
    return (foods, sure, impossible)

foods, sure, impossible = foods_possible_impossible()

def part_1():
    total = 0
    for ingredient in impossible:
        for food in foods:
            total += (1 if ingredient in food.ingredients else 0)
    print("Part 1:", total)

def part_2():
    tuples = [(item[0], list(item[1])[0]) for item in sure.items()]
    return ",".join(map(lambda tup: tup[1], list(sorted(tuples, key=lambda tup: tup[0]))))
