import sys

input = sys.stdin.readline

result, cnt = 0, 0

for _ in range(10):
    a, b = map(int, input().split())
    
    cnt += b - a
    result = max(result, cnt)
    
print(result)    