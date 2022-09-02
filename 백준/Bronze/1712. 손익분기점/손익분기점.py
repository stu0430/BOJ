import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

if c > b:
    x = a // (c - b)
    print(x + 1)
else:
    print(-1)