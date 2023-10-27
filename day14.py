from aoc import non_blank_lines
import re

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

class Machine:

    mem_pattern = re.compile(r"mem\[(\d+)] = (\d+)")
    
    def __init__(self):
        self.memory = {}
        self.mask = {}

    def where_mask_is(self, v):
        return list(map(lambda item: item[0], filter(lambda tup: tup[1] == v, self.mask.items())))
    
    def decode(self, instruction):
        if instruction[0:3] == 'mem':
            self.set_memory(instruction)
        else:
            self.set_mask(instruction)
            
    def set_mask(self, instruction):
        self.mask = {}
        mask_str = instruction.replace('mask = ', '')
        for idx, s in enumerate(reversed(mask_str)):
            if s in ['0', '1']:
                self.mask[idx] = int(s)
            else:
                self.mask[idx] = 2

    def set_memory(self, instruction):
        m = Machine.mem_pattern.match(instruction)
        self.write_memory(int(m.group(1)), int(m.group(2)))
        
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
            rest = locations[1:]
            new_addresses = []
            for address in addresses:
                new_addresses.append(set_bit(address, loc))
                new_addresses.append(clear_bit(address, loc))
                
            return Machine2.set_all_bits(rest, new_addresses)
        return addresses
    
    def write_memory(self, address, val):
        for loc in self.where_mask_is(1):
            address = set_bit(address, loc)

        for address in Machine2.set_all_bits(self.where_mask_is(2), [address]):
            self.memory[address] = val
        
instructions = non_blank_lines('input/day14.txt')
print("Part 1:", sum(Machine().run(instructions).memory.values()))
print("Part 2:", sum(Machine2().run(instructions).memory.values()))
