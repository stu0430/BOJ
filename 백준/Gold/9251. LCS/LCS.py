import sys

input = sys.stdin.readline

n = input().rstrip()
m = input().rstrip()

d = [[0] * (len(m) + 1) for i in range(len(n) + 1)]

for i in range(1, len(n) + 1):
    for j in range(1, len(m) + 1):
        if n[i - 1] == m[j - 1]:
            d[i][j] = d[i - 1][j - 1] + 1
        
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[-1][-1])