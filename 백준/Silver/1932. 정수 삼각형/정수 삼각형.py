import sys

input = sys.stdin.readline

n = int(input())

d = [[0] * (i + 1) for i in range(n)]

for i in range(n):
    d[i] = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            d[i][j] = d[i - 1][j] + d[i][j]
        elif j == i:
            d[i][j] = d[i - 1][j - 1] + d[i][j]
        else:
            d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + d[i][j]

print(max(d[n - 1]))