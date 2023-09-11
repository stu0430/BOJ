import sys

input = sys.stdin.readline

y, m, d = map(int, input().rstrip().split('-'))
n = int(input())

d += n

if d > 30:
    m += d // 30
    d %= 30

    if m > 12:
        y += m // 12
        m %= 12

if d == 0:
    d = 30
    m -= 1

if m == 0:
    m = 12 
    y -= 1

print(f'{y}-{m:02d}-{d:02d}')          