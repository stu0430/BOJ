import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
result = s + [0] * m

for i in range(n):
    t = list(map(int, input().split()))
    result[i] -= sum(t)
    for j in range(n + m):
        result[j] += t[j]
        
print(*result)