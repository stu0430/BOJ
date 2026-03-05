import sys

input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
result = 0

for _ in range(p):
    px, py = map(int, input().split())
    r = (h / 2) ** 2

    if x <= px <= x + w and y <= py <= y + h:
        result += 1

    elif ((px - x) ** 2 + (py - (y + h / 2)) ** 2) <= r:
        result += 1

    elif ((px - (x + w)) ** 2 + (py - (y + h / 2)) ** 2) <= r:
        result += 1

print(result)