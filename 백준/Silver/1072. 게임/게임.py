import sys
import math

input = sys.stdin.readline

x, y = map(int, input().split())

z = y * 100 // x
result = 0

if z >= 99:
    result = -1
else:
    result = math.ceil(((z + 1) * x - (100 * y)) / (100 - (z + 1)))

print(result)