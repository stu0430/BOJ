import sys
from collections import deque

input = sys.stdin.readline

while True:
    s = input().rstrip()
    
    dq = deque()

    if s == '.':
        break

    for i in s:
        if i == '[' or i == '(':
            dq.append(i)

        elif i == ']':
            if len(dq) != 0 and dq[-1] == '[':
                dq.pop() 

            else: 
                dq.append(']')
                break

        elif i == ')':
            if len(dq) != 0 and dq[-1] == '(':
                dq.pop()

            else:
                dq.append(')')
                break

    if dq:
        print('no')

    else:
        print('yes')