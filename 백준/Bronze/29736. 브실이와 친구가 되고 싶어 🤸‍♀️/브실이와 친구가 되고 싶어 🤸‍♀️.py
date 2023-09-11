import sys

input = sys.stdin.readline

a, b = map(int, input().split())
k, x = map(int, input().split())

array = [i for i in range(a, b+1)]

cnt = 0

for i in array:
    if abs( i - k) <= x:
        cnt += 1
        
print(cnt if cnt != 0 else 'IMPOSSIBLE')