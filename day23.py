from aoc import print_assert

class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

    def __repr__(self):
        return f"Node({self.val})"
    
class Game:
    def __init__(self, size):
        self.size = size
        init = [3,6,2,9,8,1,7,5,4]
        n = []

        for i in range(0, size+1):
            n.append(Node(i))
        
        for i in range(1, size+1):
            if not i == size:
                n[i].next = n[i+1]
            else:
                n[i].next = n[1]

            if not i == 1:
                n[i].prev = n[i-1]
            else:
                n[i].prev = n[size]

        #yuck! can't think of a better way.
        for i, label in enumerate(init):
            if i == 0:
                n[label].prev = n[init[-1]] if len(init) == size else n[-1]
                n[label].next = n[init[i+1]]
                if len(init) != size:
                    n[size].next = n[label]
            elif i + 1 == len(init):
                n[label].prev = n[init[i-1]]
                n[label].next = n[init[0]] if len(init) == size else n[i+2]
                if len(init) != size:
                    n[i+2].prev = n[label]
            else:
                n[label].prev = n[init[i-1]]
                n[label].next = n[init[i+1]]
                
        self.nodes = n
        self.current = self.nodes[init[0]]
        self.init_size = len(init)

    def __str__(self):
        node = self.nodes[1]
        tmp = []
        for i in range(self.init_size-1):
            node = node.next
            tmp.append(node.val)

        return ''.join((str(i) for i in tmp))

    def destination_label(self):
        def next_val(v):
            return v-1 if v > 1 else self.size
        
        val = next_val(self.current.val)
        next_1 = self.current.next
        next_2 = next_1.next
        next_3 = next_2.next

        while(next_1.val == val or next_2.val == val or next_3.val == val):
            val = next_val(val)

        return val
        
    def move(self):
        #find destination label
        label = self.destination_label()
        
        #pickup cups
        pickup_start = self.current.next
        pickup_next = pickup_start.next
        pickup_end = pickup_next.next

        #maintain the circle
        self.current.next = pickup_end.next

        #splice in
        dest = self.nodes[label]
        pickup_end.next = dest.next
        dest.next.prev = pickup_end
        dest.next = pickup_start
        pickup_start.prev = dest

        self.current = self.current.next
        return self

    def move_times(self, num):
        for i in range(num):
            self.move()
        return self

print_assert("Part 1:", str(Game(9).move_times(100)), '24798635')

def part_2():
    game = Game(1000000).move_times(10000000)
    return game.nodes[1].next.val * game.nodes[1].next.next.val

print_assert("Part 2:", part_2(), 12757828710)
