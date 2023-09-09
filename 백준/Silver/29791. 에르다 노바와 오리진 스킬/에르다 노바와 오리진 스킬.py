import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

x, y = 1, 1

t = a[0]
for i in range(1, n):
    if t + 100 <= a[i]:
        x += 1
        t = a[i]

t = b[0]
for i in range(1, m):
    if t + 360 <= b[i]:
        y += 1
        t = b[i]
        
print(x, y)