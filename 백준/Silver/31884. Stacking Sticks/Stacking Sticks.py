import sys

input = sys.stdin.readline

q = int(input())

b = {}

for _ in range(q):
    n, i = map(int, input().split())
    if n == 1:
        for j in range(i, i + 4):
            if j not in b:
                b[j] = 0
        
        maximum = max(b[i], b[i + 1], b[i + 2], b[i + 3])
        for j in range(i, i + 4):
            b[j] = maximum + 1
    
    elif n == 2:
        if i not in b:
            b[i] = 4
        
        else:
            b[i] += 4
    
    else:
        if i not in b:
            print(0)
        
        else:
            print(b[i])