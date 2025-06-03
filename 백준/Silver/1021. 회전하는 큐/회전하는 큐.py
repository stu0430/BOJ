import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
dq = deque([i for i in range(1, n + 1)])
index = list(map(int,input().split()))

result = 0

for i in index:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        
        else:
            if dq.index(i) <= len(dq) // 2:
                dq.rotate(-1)
                result += 1
                
            else:
                dq.rotate(1)
                result += 1

print(result)