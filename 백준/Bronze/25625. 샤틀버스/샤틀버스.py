import sys

input = sys.stdin.readline

x, y = map(int, input().split())

if y < x :
    print(x + y)
elif y > x:
    print(y - x)