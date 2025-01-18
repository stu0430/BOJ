import sys
from collections import deque

input = sys.stdin.readline

n, k, m = map(int,input().split())

dq = deque(i + 1 for i in range(n))
result = []
num = 0

for _ in range(n):
    if (num // m) % 2 == 1:
        dq.rotate(k)
        result.append(dq.popleft())
        
    else:
        dq.rotate(-(k - 1))
        result.append(dq.popleft())
        
    num += 1

print(*result, sep='\n')