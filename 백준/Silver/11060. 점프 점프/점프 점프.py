import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

d = [0] * (n + 1)

for i in range(1, n):
    d[i] = 1001

for i in range(n):
    for j in range(1, array[i] + 1):
        if i + j < n:
            d[i + j] = min(d[i + j], d[i] + 1)
            
if d[n - 1] == 1001:
    print(-1)
    
else:
    print(d[n - 1])