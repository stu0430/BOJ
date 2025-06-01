import sys
from collections import deque

input = sys.stdin.readline

operator = {'+': 1, '-': 1, '*': 2, '/': 2}

infix = list(input().rstrip())
dq = deque()

postfix = []

for t in infix:
    if t == '(':
        dq.append(t)
    
    elif t == ')':
        while dq and dq[-1] != '(':
            postfix.append(dq.pop())
            
        if dq:
            dq.pop()
        
    elif t.isalpha():
        postfix.append(t)
    
    elif t in operator:
        while (dq and dq[-1] != '(' and operator.get(dq[-1]) >= operator.get(t)):
            postfix.append(dq.pop())
            
        dq.append(t)
            
while dq:
    if dq[-1] != '(':
        postfix.append(dq.pop())
    else:
        dq.pop()
    
print(''.join(postfix))