# 5430번 AC

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for i in range(t):
    p = list(input().rstrip())
    n = int(input())
    queue =  deque(input().rstrip()[1:-1].split(','))

    r = 0

    if n == 0:
        queue = []

    for j in p:
        if j == 'R':
            r += 1
        elif j == 'D':
            if not queue:
                print('error')
                break
            else:
                if r % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    
    else:
        if r % 2 == 0:
            print('[' + ','.join(queue) + ']')
        else:
            queue.reverse()
            print('[' + ','.join(queue) + ']')