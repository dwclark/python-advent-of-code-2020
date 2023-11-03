from aoc import blank_line_grouped, print_assert
from collections import deque

class Player:
    def __init__(self, num, cards):
        self.num = num
        self.cards = cards

    @staticmethod
    def new(num):
        return Player(num, deque())

    def add_cards(self, *c):
        self.cards.extend(c)

    def get_card(self):
        return self.cards.popleft()

    def score(self):
        return sum((((n+1)*c) for n, c in enumerate(reversed(self.cards))))

def load_players():
    ret = []
    for n, batch in enumerate(blank_line_grouped('input/day22.txt')):
        p = Player.new(n+1)
        for line in batch[1:]: 
            p.add_cards(int(line))
        ret.append(p)
    return ret

def play_1(p1, p2):
    while(p1.cards and p2.cards):
        c1 = p1.get_card()
        c2 = p2.get_card()
        if c1 < c2:
            p2.add_cards(c2, c1)
        else:
            p1.add_cards(c1, c2)
    return p1 if p1.cards else p2

def has_prev(list_cards, this_round):
    try:
        return next((1 for cards in this_round if list_cards == cards))
    except StopIteration:
        return False

def play_2(p1, p2):
    rounds_1 = []
    rounds_2 = []

    while p1.cards and p2.cards:
        if has_prev(list(p1.cards), rounds_1) or has_prev(list(p2.cards), rounds_2):
            return p1

        rounds_1.append(list(p1.cards))
        rounds_2.append(list(p2.cards))
        
        c1 = p1.get_card()
        c2 = p2.get_card()
        
        winner = None
        if c1 <= len(p1.cards) and c2 <= len(p2.cards):
            p1Next = Player(1, deque(list(p1.cards)[:c1]))
            p2Next = Player(2, deque(list(p2.cards)[:c2]))
            winner = play_2(p1Next, p2Next)
        else:
            winner = p2 if c1 < c2 else p1
            
        if winner.num == 1:
            p1.add_cards(c1, c2)
        else:
            p2.add_cards(c2, c1)
            
    return p1 if p1.cards else p2

print_assert("Part 1:", play_1(*load_players()).score(), 32272)
print_assert("Part 2:", play_2(*load_players()).score(), 33206)
