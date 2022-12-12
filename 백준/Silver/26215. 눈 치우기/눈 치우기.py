import sys
from math import ceil

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

result = max(max(array), ceil(sum(array) / 2))

print(-1 if result > 1440 else result)