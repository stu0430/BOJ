import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    d = [[0] * (m + 1) for i in range(n + 1)]
    
    for j in range(1, m + 1):
        d[1][j] = j
        
    for k in range(2, n + 1):
        for l in range(k, m + 1):
            d[k][l] = d[k - 1][l - 1] + d[k][l - 1]
            
    print(d[n][m])