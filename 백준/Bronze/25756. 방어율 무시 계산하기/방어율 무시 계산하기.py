import sys

input = sys.stdin.readline

n = int(input())
ignores = list(map(int, input().split()))
v = 0

for i in ignores:
    v = 1 - (1 - v) * (1 - i / 100)
    print(v * 100)