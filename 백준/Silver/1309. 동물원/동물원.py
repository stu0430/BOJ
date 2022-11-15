import sys

input = sys.stdin.readline

n = int(input())

d = [1, 1, 1]

for i in range(2, n +1):
    d[0], d[1], d[2] = sum(d) % 9901, (d[0] + d[1]) % 9901, (d[0] + d[1]) % 9901

print(sum(d) % 9901)