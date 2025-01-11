import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 1000001

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in a:
    d[i] += 1

result = 0

for i in b:
    if d[i] >= 1:
        d[i] -= 1
    
    else :
        result += 1

print(result)