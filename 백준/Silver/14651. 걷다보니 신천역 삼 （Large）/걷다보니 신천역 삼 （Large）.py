import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 33334

d[1] = 0
d[2] = 2
d[3] = 6

for i in range(4, n + 1):
    d[i] = (d[i - 1] * 3) % 1000000009

print(d[n])