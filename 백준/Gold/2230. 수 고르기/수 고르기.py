import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

array.sort()

start = 0
end = 0
result = float('inf')

while start < n and end < n:
    if array[end] - array[start] < m:
        end += 1
    else:
        result = min(result, array[end] - array[start])
        start += 1

print(result)