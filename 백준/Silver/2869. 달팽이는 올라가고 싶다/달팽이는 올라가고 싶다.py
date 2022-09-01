import sys

input = sys.stdin.readline

a, b, v = map(int, input().split())
gap = a - b
x = (v - b) % gap

if x == 0:
    print((v - b) // gap)
else:
    print(((v - b) // gap) + 1)