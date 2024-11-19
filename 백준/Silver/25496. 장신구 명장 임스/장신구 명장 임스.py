import sys

input = sys.stdin.readline

p, n = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

cnt = 0

for i in a:
    if p >= 200:
        break
    
    else:
        p += i
        cnt += 1
    
print(cnt)