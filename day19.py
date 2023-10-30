from aoc import blank_line_grouped
import regex

class Single:
    def __init__(self, char):
        self.char = char

class All:
    def __init__(self, data):
        if isinstance(data, str):
            self.data = [int(c) for c in data.split(' ')]
        else:
            self.data = data

    def lookup(self, all_matchers):
        def to_matcher(o):
            if isinstance(o, Maybe):
                return o
            else:
                return all_matchers[o]
                
        return [ to_matcher(o) for o in self.data ]

class Any:
    def __init__(self, data):
        self.data = data

class Maybe:
    def __init__(self, num):
        self.num = num
    
    def lookup(self, all_matchers):
        return [ all_matchers[self.num] ]

def make_single(raw):
    num = int(raw[:raw.index(':')])
    raw_rule = raw[(raw.index(':') + 1):].strip()
    
    if raw_rule.find('"') != -1:
        return (num, Single(raw_rule.replace('"', '')))
    elif raw_rule.find('|') != -1:
        return (num, Any([All(s) for s in raw_rule.split(' | ')]))
    else:
        return (num, All(raw_rule))
    
def make_all(raw):
    return { tup[0]:tup[1] for tup in [make_single(s) for s in raw] }

def match(list_matchers, message, all_matchers):
    if list_matchers and not message:
        return None
    elif not list_matchers:
        return message

    current = list_matchers[0]
    if isinstance(current, Single) and current.char == message[0]:
        return match(list_matchers[1:], message[1:], all_matchers)
    elif isinstance(current, All):
        return match(current.lookup(all_matchers) + list_matchers[1:], message, all_matchers)
    elif isinstance(current, Maybe):
        m = match(list_matchers[1:], message, all_matchers)
        if not m is None:
            return m
        else:
            return match(current.lookup(all_matchers) + list_matchers[1:], message, all_matchers)
    elif isinstance(current, Any):
        for matcher in current.data:
            m = match([matcher] + list_matchers[1:], message, all_matchers)
            if not m is None:
                return m
        return None
    
def count_matching(matcher, matchers, messages):
    return sum([ 1 if match([matcher], m, matchers) == '' else 0 for m in messages ])

batches = blank_line_grouped('input/day19.txt')
raw_rules = batches[0]
messages = batches[1]
matchers = make_all(raw_rules)

print("Part 1:", count_matching(matchers[0], matchers, messages))

p2_matchers = dict(matchers)
p2_matchers[8] = All([42, Maybe(8)])
p2_matchers[11] = All([42, Maybe(11), 31])

print("Part 2:", count_matching(matchers[0], p2_matchers, messages))
