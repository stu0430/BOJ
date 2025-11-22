import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

a.sort()
total = 0
i = 0
while i < n and a[i] < 0:
    total += (-a[i])
    i += k

i = n - 1
while i >= 0 and a[i] > 0:
    total += a[i]
    i -= k

print(total * 2)