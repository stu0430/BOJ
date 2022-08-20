import sys
from collections import deque

input = sys.stdin.readline
dq = deque()
n = int(input())

for i in range(n):
    p = input().rstrip()

    if ' ' in p:
        p, n = p.split()
        n = int(n)

    if p == 'push_front':
        dq.appendleft(n)

    elif p == 'push_back':
        dq.append(n)
    
    elif p == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
            
    elif p == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    elif p == 'size':
        print(len(dq))

    elif p == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif p == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    elif p == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
