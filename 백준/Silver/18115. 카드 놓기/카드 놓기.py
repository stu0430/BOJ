import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

dq = deque()

for i in range(n):
    if array[n - 1 - i] == 1:
        dq.appendleft(i + 1)
        
    elif array[n - 1 - i] == 2:
        x = dq.popleft()
        dq.appendleft(i + 1)
        dq.appendleft(x)
        
    elif array[n - 1 - i] == 3:
        dq.append(i + 1)
        
print(*dq)