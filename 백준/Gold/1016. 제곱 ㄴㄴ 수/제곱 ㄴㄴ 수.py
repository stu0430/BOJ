import sys

input = sys.stdin.readline

min_n, max_n = map(int, input().split())

d = [False] * (max_n - min_n + 1)

for i in range(2, int(max_n ** 0.5) + 1):
    square = i ** 2
    start = min_n // square
    
    if min_n % square != 0:
        start += 1
        
    for j in range(start, (max_n // square) + 1):
        d[(j * square) - min_n] = True
        
print(d.count(False))