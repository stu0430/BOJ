import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

result = 0

for i in range(n):
    if array[i] in array[:i]:
        result += 1
        
    else:
        continue
    
print(result)