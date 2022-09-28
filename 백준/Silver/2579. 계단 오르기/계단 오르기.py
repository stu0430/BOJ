import sys

input = sys.stdin.readline

n = int(input())

array = [0] * 301

for i in range(n):
    array[i] = int(input())

d = [0] * 301

d[0] = array[0]
d[1] = array[0] + array[1]
d[2] = max(array[0] + array[2], array[1] + array[2])

for i in range(3, n):
    d[i] = max(d[i - 3] + array[i - 1] + array[i], d[i - 2] + array[i])

print(d[n - 1])