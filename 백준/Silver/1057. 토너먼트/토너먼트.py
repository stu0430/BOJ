import sys

input = sys.stdin.readline

n, k, h = map(int, input().split())

count = 0

while k != h:
    k = k // 2 + k % 2
    h = h // 2 + h % 2
    count += 1
    
print(count)