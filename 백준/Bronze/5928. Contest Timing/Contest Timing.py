import sys

input = sys.stdin.readline
    
d, h, m = map(int, input().split())

t = (d * 24 * 60 + h * 60 + m) - (11 * 24 * 60 + 11 * 60 + 11)

if t < 0:
    print(-1)
    
else:
    print(t)