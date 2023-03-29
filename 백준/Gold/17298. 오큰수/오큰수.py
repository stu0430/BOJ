import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

stack = []
result = [-1] * n

for i in range(n):
    while stack and array[stack[-1]] < array[i]:
        result[stack.pop()] = array[i]
        
    stack.append(i)

print(*result)