from aoc import non_blank_lines, set_bit, clear_bit
import re

class Machine:

    mem_pattern = re.compile(r"mem\[(\d+)] = (\d+)")
    mask_pattern = re.compile(r"mask = ([X01]{36})")
    
    def __init__(self):
        self.memory = {}
        self.mask = {}

    def where_mask_is(self, v):
        return list(map(lambda item: item[0], filter(lambda tup: tup[1] == v, self.mask.items())))
    
    def decode(self, instruction):
        match = Machine.mem_pattern.match(instruction)
        if match:
            self.write_memory(int(match.group(1)), int(match.group(2)))
        else:
            self.set_mask(Machine.mask_pattern.match(instruction).group(1))
            
    def set_mask(self, mask_str):
        self.mask = {}
        for idx, s in enumerate(reversed(mask_str)):
            self.mask[idx] = int(s) if s in ['0','1'] else 2

    def write_memory(self, address, val):
        for loc in self.where_mask_is(0):
            val = clear_bit(val, loc)

        for loc in self.where_mask_is(1):
            val = set_bit(val, loc)

        self.memory[address] = val

    def run(self, instructions):
        for instruction in instructions:
            self.decode(instruction)
        return self

class Machine2(Machine):

    @staticmethod
    def set_all_bits(locations, addresses):
        if locations:
            loc = locations[0]
            new_addresses = []
            for address in addresses:
                new_addresses.extend([set_bit(address, loc), clear_bit(address, loc)])
                
            return Machine2.set_all_bits(locations[1:], new_addresses)
        return addresses
    
    def write_memory(self, address, val):
        for loc in self.where_mask_is(1):
            address = set_bit(address, loc)

        for address in Machine2.set_all_bits(self.where_mask_is(2), [address]):
            self.memory[address] = val
        
instructions = non_blank_lines('input/day14.txt')
print("Part 1:", sum(Machine().run(instructions).memory.values()))
print("Part 2:", sum(Machine2().run(instructions).memory.values()))
