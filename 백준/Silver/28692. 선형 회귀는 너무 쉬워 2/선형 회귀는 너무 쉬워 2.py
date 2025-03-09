import sys

input = sys.stdin.readline

n = int(input())

x, y, xy, xx = 0, 0, 0, 0

for _ in range(n):
    x_i, y_i = map(int, input().split())
    
    x += x_i
    y += y_i
    
    xy += x_i * y_i
    xx += x_i ** 2
    
if x ** 2 != n * xx:
    a = (n * xy - x * y) / (n * xx - x ** 2)
    b = (y - a * x) / n
    print(a, b)
    
else:
    print('EZPZ')