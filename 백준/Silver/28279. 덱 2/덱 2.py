import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    c = input().rstrip().split()
    
    if len(c) == 2:
        op, x = c[0], c[1]
        
        if op == '1':
            dq.appendleft(x)
            
        elif op == '2':
            dq.append(x)
            
    else:
        op = c[0]
        
        if op == '3':
            print(dq.popleft() if dq else -1)
            
        elif op == '4':
            print(dq.pop() if dq else -1)
            
        elif op == '5':
            print(len(dq))
            
        elif op == '6':
            print(0 if dq else 1)
            
        elif op == '7':
            print(dq[0] if dq else -1)
            
        elif op == '8':
            print(dq[-1] if dq else -1)