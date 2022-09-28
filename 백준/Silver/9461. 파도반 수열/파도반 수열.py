import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    d = [0] * 101
    
    d[1] = 1
    d[2] = 1
    
    n = int(input())
    
    for i in range(3, n + 1):
        d[i] = d[i - 2] + d[i - 3]
        
    print(d[n])