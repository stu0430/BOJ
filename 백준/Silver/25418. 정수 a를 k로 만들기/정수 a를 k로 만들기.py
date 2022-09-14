import sys

input = sys.stdin.readline

a, k = map(int, input().split())

cnt = 0

while a != k:
    if a * 2 <= k and k % 2 == 0:
        k //= 2    
    else:
          k -= 1
    cnt += 1
    
print(cnt)