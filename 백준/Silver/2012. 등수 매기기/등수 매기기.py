import sys

input = sys.stdin.readline

n = int(input())

array = [int(input()) for i in range(n)]

array = sorted(array)

result = 0

for i in range(n):
    result += abs(array[i] - (i + 1))
    
print(result)