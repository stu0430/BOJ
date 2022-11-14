import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    queue = deque([(i, idx) for idx, i in enumerate(array)])
    count = 0
    
    while queue:
        if queue[0][0] == max(queue)[0]:
            count += 1
            
            if queue[0][1] == m:
                print(count)
                break
            
            else:
                queue.popleft()
                
        else:
            queue.append(queue.popleft())