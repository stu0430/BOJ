import sys

input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

result = 0

for i in range(k):
    result += array[i]

temp = result

for i in range(k, n):
    temp += array[i] - array[i - k]
    result = max(result, temp)

print(result)