from aoc import non_blank_lines, print_assert
from functools import reduce

class Food:
    def __init__(self, line):
        groups = line.split('(contains')
        self.ingredients = set(groups[0].strip().split(' '))
        self.allergens = set(groups[1].replace(')', '').strip().split(', '))

def initial_possible(foods):
    table = {}
    for food in foods:
        for allergen in food.allergens:
            table[allergen] = table[allergen] & food.ingredients if allergen in table.keys() else food.ingredients
    return table

def for_sure(possible):
    working = copy.deepcopy(possible)
    find_matching = lambda fun: dict(filter(fun , working.items()))
    find_singles = lambda: find_matching(lambda item: len(item[1]) == 1)
    find_multiples = lambda: find_matching(lambda item: len(item[1]) > 1)
    
    singles, multiples = find_singles(), find_multiples()
    
    while len(working) != len(singles):
        for allergen, ingredients in singles.items():
            ingredient = next(iter(ingredients))
            for mult_allergen, mult_ingredients in multiples.items():
                working[mult_allergen].discard(ingredient)
        singles, multiples = find_singles(), find_multiples()

    return working

def foods_possible_impossible():
    foods = [Food(line) for line in non_blank_lines('input/day21.txt')]
    sure = for_sure(initial_possible(foods))
    all_ingredients = reduce(lambda s1, s2: s1 | s2, [food.ingredients for food in foods], set())
    impossible = all_ingredients - reduce(lambda s1, s2: s1 | s2, sure.values(), set())
    return (foods, sure, impossible)

foods, sure, impossible = foods_possible_impossible()

def part_1():
    return sum((1 for ingredient in impossible
                for food in foods if ingredient in food.ingredients))

def part_2():
    tuples = [(item[0], list(item[1])[0]) for item in sure.items()]
    return ",".join(map(lambda tup: tup[1], list(sorted(tuples, key=lambda tup: tup[0]))))

print_assert("Part 1:", part_1(), 1930)
print_assert("Part 2:", part_2(), 'spcqmzfg,rpf,dzqlq,pflk,bltrbvz,xbdh,spql,bltzkxx')
