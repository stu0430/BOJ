import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

count, result = 0, 0

for i in range(n):
    if array[i] == 1:
        count += 1
        result += count
        
    else:
        count = 0

print(result)