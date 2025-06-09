import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

dq = deque([b[i] for i in range(n) if a[i] == 0])

for i in range(m):
    dq.appendleft(c[i])
    
    print(dq.pop(), end= ' ')