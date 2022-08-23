import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for i in range(t):
    dq = deque()
    X = False
    parenthesis = input().rstrip()
    
    for j in parenthesis:
        if j == '(':
            dq.append(j)
            
        elif j == ')':
            if len(dq) == 0:
                X = True
                break
            else:
                dq.pop()
                
    if X or len(dq) != 0:
        print('NO')
        
    else:
        print('YES')