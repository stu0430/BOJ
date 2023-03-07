import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, d = map(int, input().split())
    
    count = 0
    
    for j in range(n):
        v, f, c = map(int, input().split())
        
        if v * f / c >= d:
            count += 1
            
    print(count)