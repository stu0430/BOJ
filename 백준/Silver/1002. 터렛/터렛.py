import sys

input = sys.stdin.readline

t = int(input())
    
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    r = [r1, r2, d]
    r.sort()
    
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r[2] == r[0] + r[1]:
            print(1)
        elif r[2] > r[0] + r[1]:
            print(0)
        else:
            print(2)