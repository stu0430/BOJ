import sys

input = sys.stdin.readline

n = int(input())
array = list(input().strip())
CHANGE = {'R': 'G', 'G': 'B', 'B': 'R'}

result = float('inf')

for start_changes in range(3):
    lights = array.copy()
    
    for _ in range(start_changes):
        for i in range(3):
            lights[i] = CHANGE[lights[i]]
    
    count = start_changes
    
    for i in range(1, n - 2):
        while lights[0] != lights[i]:
            count += 1
            for j in range(i, i + 3):
                lights[j] = CHANGE[lights[j]]
    
    if lights[0] == lights[-1] == lights[-2]:
        result = min(result, count)

print(result if result != float('inf') else -1)