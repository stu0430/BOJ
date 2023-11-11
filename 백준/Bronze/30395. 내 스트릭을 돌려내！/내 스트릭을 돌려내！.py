import sys

input = sys.stdin.readline

n = int(input())

problems = list(map(int, input().split()))
s, c, f = 0, 0, -2

for i, p in enumerate(problems):
    if p:
        c += 1

    elif i - f >= 2:
        f = i

    else:
        s = max(s, c)
        c = 0

s = max(s, c)
print(s)