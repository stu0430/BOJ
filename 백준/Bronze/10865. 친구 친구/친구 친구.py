import sys

input = sys.stdin.readline

n, m = map(int, input().split())

count = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    
    count[a] += 1
    count[b] += 1
    
for i in range(1, n + 1):
    print(count[i])