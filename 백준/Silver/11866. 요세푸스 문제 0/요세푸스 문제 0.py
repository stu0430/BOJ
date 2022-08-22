import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int, input().split())
dq = deque([i+1 for i in range(n)])
josephus = []

while dq:
    for i in range(k-1):
        dq.append(dq.popleft())
        
    josephus.append(dq.popleft())

print("<", end = '')
for i in range(n):
    if i == n - 1:
        print(josephus[i], end= '')
    else:
        print(josephus[i], end = ', ')
print(">")