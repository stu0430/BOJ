import sys

input = sys.stdin.readline

a, b = map(int, input().split())

n = int(input())

arr = [0] * n

for i in range(n):
    arr[i] = int(input())

for j in range(n):
    arr[j] = abs(b - arr[j])
    
print(min(min(arr) + 1, abs(b - a)))