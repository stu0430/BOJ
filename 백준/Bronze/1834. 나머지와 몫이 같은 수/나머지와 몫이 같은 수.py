import sys

input = sys.stdin.readline

n = int(input())

result = 0

for i in range(1, n):
    result += i * n + i
        
print(result)