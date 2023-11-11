import sys

input = sys.stdin.readline

n = int(input())
x, y = set(), set()

while n:
    n -= 1
    dx, dy = map(int, input().split())
    x.add(dx)
    y.add(dy)

print(max(y) - min(y))