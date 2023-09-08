import sys

input = sys.stdin.readline

n, k, x = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
lst = [array[i][0] for i in range(n)]

d = [[False] * (n * x + 1) for _ in range(n + 1)]
d[0][0] = True

for i in range(n):
    for j in range(min(i + 1, k), 0, -1):
        for l in range(x * j, lst[i] - 1, -1):
            d[j][l] = (d[j][l] or d[j - 1][l - lst[i]])

result = 0

for i in range(k * x + 1):
    if d[k][i]:
        result = max(result, i * (k * x - i))

print(result)