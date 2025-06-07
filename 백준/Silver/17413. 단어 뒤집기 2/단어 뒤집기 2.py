import sys
from collections import deque

input = sys.stdin.readline

s = input().rstrip()
dq = deque(s)
stack = deque()

while dq:
    token = dq[0]
    
    if token == '<':
        if stack:
            while stack:
                print(stack.pop(), end='')
                
        while dq[0] != '>':
            print(dq.popleft(), end='')
            
        print(dq.popleft(), end='')
            
    elif token == ' ':
        if stack:
            while stack:
                print(stack.pop(), end='')
                
        print(dq.popleft(), end='')
        
    else:
        stack.append(dq.popleft())

if stack:
    while stack:
        print(stack.pop(), end='')