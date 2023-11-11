import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dq = deque()

for _ in range(n):
    p = input().rstrip().split()

    if p[0] == '1':
        dq.append(int(p[1]))

    elif p[0] == '2':
        if dq:
            print(dq.pop())
        else:
            print(-1)

    elif p[0] == '3':
        print(len(dq))

    elif p[0] == '4':
        if dq:
            print(0)
        else:
            print(1)

    elif p[0] == '5':
        if dq:
            print(dq[-1])
        else:
            print(-1)