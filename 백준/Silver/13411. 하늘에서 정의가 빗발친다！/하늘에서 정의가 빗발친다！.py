import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())
array = []

for i in range(1, n + 1):
    x, y, v = map(float, input().split())
    array.append((sqrt(x * x + y * y) / v, i))

array.sort()

for _, i in array:
    print(i)