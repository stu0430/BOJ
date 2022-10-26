import sys

input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))

d = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + p[j])

print(d[n])