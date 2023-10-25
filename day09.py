from aoc import single_int_line
from itertools import combinations

def search_violation(window_size, the_list):
    for index in range(window_size, len(the_list)):
        current = the_list[index]
        found = False
        sliced = the_list[(index-window_size):index]

        for tup in combinations(sliced, 2):
            if tup[0] + tup[1] == current:
                found = True
                break

        if not found:
            return current

def search_for_sum(look_for, the_list):
    for low in range(0, len(the_list)):
        tot = the_list[low]
        for high in range(low+1, len(the_list)):
            tot += the_list[high]
            if look_for < tot:
                break
            elif tot == look_for:
                sliced = sorted(the_list[low:(high+1)])
                return sliced[0] + sliced[-1]
        
my_list = single_int_line('input/day09.txt')

print("Part 1:", search_violation(25, my_list))
print("Part 2:", search_for_sum(177777905, my_list))
