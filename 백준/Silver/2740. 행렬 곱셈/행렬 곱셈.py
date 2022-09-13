import sys

input = sys.stdin.readline

a = []
b = []

n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

m, k = map(int, input().split())
for j in range(m):
    row = list(map(int, input().split()))
    b.append(row)

matrix = [[0 for i in range(k)] for j in range(n)]

for i in range(n):
    for j in range(k):
        x = []
        for l in range(m):
            x.append(a[i][l] * b[l][j])
        matrix[i][j] = sum(x)

for i in matrix:
    print(*i)