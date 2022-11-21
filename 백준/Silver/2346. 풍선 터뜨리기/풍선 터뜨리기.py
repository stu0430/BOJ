import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))
queue = deque([(i, idx) for idx, i in enumerate(array)])

while queue:
    if len(queue) == 1:
        print(queue[0][1] + 1)
        break
        
    else:
        print(queue[0][1] + 1, end = ' ')
        move = queue[0][0]
        queue.popleft()
        
        if move > 0:
            for i in range(move - 1):
                queue.append(queue.popleft())
                
        else:
            for i in range(abs(move)):
                queue.appendleft(queue.pop())