import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

idx = 0
result = int(1e9)

for i in range(257):
    min_h, max_h = 0, 0

    for x in range(n):
        for y in range(m):
            if g[x][y] >= i:
                max_h += g[x][y] - i

            else:
                min_h += i - g[x][y]

    if max_h + b >= min_h:
        if min_h + (max_h * 2) <= result:
            result = min_h + (max_h * 2)
            idx = i

print(result, idx)