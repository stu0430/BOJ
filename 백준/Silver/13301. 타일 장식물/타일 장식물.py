import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 81

d[1] = 4
d[2] = 6

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
    
print(d[n])