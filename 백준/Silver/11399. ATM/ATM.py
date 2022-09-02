import sys

input = sys.stdin.readline

n = int(input())
arr = [0] * n 

p = list(map(int, input().split()))
p.sort()

for i in range(n):
    arr[i] = sum(p[:i+1])
    
print(sum(arr))