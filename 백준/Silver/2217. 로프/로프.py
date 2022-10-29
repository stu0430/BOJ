import sys

input = sys.stdin.readline

n = int(input())

array = [int(input()) for i in range(n)]

array.sort(reverse=True)

result = 0

for i in range(n):
    result = max(result, array[i] * (i + 1))

print(result)