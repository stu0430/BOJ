import sys
from collections import deque

input = sys.stdin.readline

a, b, c = map(int, input().split())
capacity = [a, b, c]
visited = {(0, 0, c)}
queue = deque([(0, 0, c)])

while queue:
    state = queue.popleft()
    
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            
            new_state = list(state)
            pour = min(state[i], capacity[j] - state[j])
            new_state[i] -= pour
            new_state[j] += pour
            
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

result = sorted({c for a, b, c in visited if a == 0})
print(*result)