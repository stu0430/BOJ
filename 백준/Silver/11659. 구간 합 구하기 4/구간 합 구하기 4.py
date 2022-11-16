import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = [0] * (n + 1)
s = [0] * (n + 1)

array = list(map(int, input().split()))

for i in range(1, n + 1):
    a[i] = array[i - 1]
    
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]

for i in range(m):
    x, y = map(int, input().split())
    print(s[y] - s[x - 1])