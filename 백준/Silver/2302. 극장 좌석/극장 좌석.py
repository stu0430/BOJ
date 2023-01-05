import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

d = [1] * 41

for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]

piv = 0
result = 1

for i in range(m):
    num = int(input())
    
    result *= d[num - piv - 1]
    
    piv = num
    
result *= d[n - piv]

print(result)