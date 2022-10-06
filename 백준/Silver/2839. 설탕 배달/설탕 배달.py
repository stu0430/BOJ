import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 5001

d[3] = 1

for i in range(5, n + 1):
    if d[i - 3] != 0:
        d[i] = d[i - 3] + 1
        
    if i % 5 == 0:
        d[i] = i // 5
        
if d[n] == 0:
    print(-1)
else:
    print(d[n])