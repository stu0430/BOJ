import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 1516

for i in range(2, 1516):
    if i % 2 == 0:
        d[i] = (2 * d[i-1] + 1) % 1000000007
    else:
        d[i] = (2 * d[i-1] - 1) % 1000000007 
        
print(d[n])