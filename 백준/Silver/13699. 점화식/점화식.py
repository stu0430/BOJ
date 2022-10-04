import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 36

d[0] = 1

for i in range(1, n + 1):
    for j in range(i):
        d[i] += d[j] * d[i - j - 1]

print(d[n])