import sys

input = sys.stdin.readline

n = int(input())

array = [int(input()) for _ in range(n)]

array.sort()

count = 1
max_count = 1
result = array[0]

for i in range(1, n):
    if array[i] == array[i - 1]:
        count += 1
        
    else:
        count = 1
        
    if count > max_count:
        max_count = count
        result = array[i]
        
print(result)