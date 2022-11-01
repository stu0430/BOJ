import sys

input = sys.stdin.readline

t= int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    
    for j in range(n):
        cx, cy, r = map(int, input().split())
        
        if (cx - x1) ** 2 + (cy - y1) ** 2 < r ** 2:
            if (cx - x2) ** 2 + (cy - y2) ** 2 > r ** 2:
                count += 1
        elif (cx - x2) ** 2 + (cy - y2) ** 2 < r ** 2:
            if (cx - x1) ** 2 + (cy - y1) ** 2 > r ** 2:
                count += 1
                
    print(count)