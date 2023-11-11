import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

cur = 1
result = []
flag = True

dq = deque()

for i in range(n):
    num = int(input())

    while cur <= num:
        dq.append(cur)
        result.append('+')
        cur += 1

    if dq[-1] == num:
        dq.pop()
        result.append('-')

    else:
        print('NO')
        flag = False
        break

if flag:
    print(*result, sep='\n')