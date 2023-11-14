import sys

input = sys.stdin.readline

t = int(input())

score = 0
x, y = -2, -2

for _ in range(t):
    l, r = map(int, input().split())

    if l != 0 and l == x :
        score += 1

    if r != 0 and r == y:
        score += 1

    x, y = l, r

    if  l != 0 and r != 0 and l == r:
        score += 1

print(score)