from aoc import non_blank_lines
from collections import deque

expressions = non_blank_lines('input/day18.txt')
ops = { '+': (lambda op1, op2: op1 + op2),
        '*': (lambda op1, op2: op1 * op2) }

def tokenize(s):
    s = s.replace(")", " )").replace("(", "( ")
    return [ int(tok) if tok.isnumeric() else tok for tok in s.split(' ') ]

def to_postfix(tokens, precedence):
    stack = []
    queue = deque()
    
    for token in tokens:
        if token in ops.keys():
            pr = precedence[token]
            while stack and stack[-1] in ops.keys() and pr <= precedence[stack[-1]]:
                queue.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                queue.append(stack.pop())
            stack.pop()
        else:
            queue.append(token)

    while stack:
        queue.append(stack.pop())

    return queue

def execute_postfix(queue):
    stack = []
    while queue:
        token = queue.popleft()
        if isinstance(token, int):
            stack.append(token)
        elif token in ops.keys():
            stack.append(ops[token](stack.pop(), stack.pop()))
    return stack.pop()

def execute(precedence):
    return sum([ execute_postfix(to_postfix(tokenize(expr), precedence)) for expr in expressions ])

print("Part 1:", execute({ '+': 1, '*': 1 }))
print("Part 2:", execute({ '+': 2, '*': 1 }))
