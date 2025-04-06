import sys

input = sys.stdin.readline

n = int(input())

x, y = 1, 1
result = 0

if n == 1 or n == 2:
    result = 1
    
else:
    for i in range(3, n + 1):
        result = (x + y) % 1000000007
        x = y
        y = result

print(result, n - 2)