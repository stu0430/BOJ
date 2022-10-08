import sys

input = sys.stdin.readline

n, q = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = d[i - 1] + a[i - 1]
    
for i in range(q):
    l, r = map(int, input().split())
    print(d[r] - d[l - 1])