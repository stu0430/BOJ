import sys

input = sys.stdin.readline

n, k = map(int, input().split())

array = list(map(int, input().split()))
array.sort()

result, arcane = 0, 0

for i in range(n):
    result += array[i] * arcane
    
    if arcane < k:
        arcane += 1
    
print(result)