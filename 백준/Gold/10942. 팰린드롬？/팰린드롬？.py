import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

m = int(input())

d = [[0] * n for i in range(n)]

for i in range(n):
    d[i][i] = 1

for i in range(n - 1):
    if array[i] == array[i + 1]:
        d[i][i + 1] = 1

for k in range(3, n + 1):
    for i in range(n - k + 1):
        j = i + k - 1
        if array[i] == array[j] and d[i + 1][j - 1]:
            d[i][j] = 1
            
for i in range(m):
    s, e = map(int, input().split())
    if d[s - 1][e - 1]:
        print('1')
    else:
        print('0')