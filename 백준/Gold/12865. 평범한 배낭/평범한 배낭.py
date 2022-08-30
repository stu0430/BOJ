import sys

input = sys.stdin.readline

n, k = map(int, input().split())

value = [0] * (k+1)
items = []

for i in range(n):
    w, v = map(int, input().split())
    items.append([w, v])

for j in items:
    w, v = j
    for l in range(k, w-1, -1):
        value[l] = max(value[l], value[l-w]+v)
        
print(value[-1])