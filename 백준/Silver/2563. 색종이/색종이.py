import sys

input = sys.stdin.readline

n = int(input())

array = [[0] * 100 for i in range(100)]

for i in range(n):
    a, b = map(int, input().split())
    
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            array[i][j] = 1
            
result = 0

for i in array:
    result += sum(i)

print(result)