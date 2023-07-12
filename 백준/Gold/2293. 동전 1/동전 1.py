import sys

input = sys.stdin.readline

n, k = map(int, input().split())

d = [0] * 10001

d[0] = 1

c =  [int(input()) for i in range(n)]

for i in c:
    for j in range(1, k + 1):
        if j - i >= 0:
            d[j] += d[j - i]

print(d[k])