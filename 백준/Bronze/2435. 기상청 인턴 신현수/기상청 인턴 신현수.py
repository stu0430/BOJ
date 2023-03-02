import sys

input = sys.stdin.readline

n, k = map(int, input().split())

array = list(map(int, input().split()))

result = [sum(array[i:i + k]) for i in range(n - k + 1)]

print(max(result))