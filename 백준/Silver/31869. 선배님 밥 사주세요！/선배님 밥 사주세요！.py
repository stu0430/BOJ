import sys

input = sys.stdin.readline

n = int(input())

log = {}
for _ in range(n):
    s, w, d, p = input().split()
    log[s] = [(int(w) - 1) * 7 + int(d), int(p)]

data = [0] * 70
for _ in range(n):
    s, m = input().split()
    if int(m) - log[s][1] >= 0:
        data[log[s][0]] = True

max_count = 0
current_count = 0
for day in data:
    if day:
        current_count += 1
    else:
        max_count = max(max_count, current_count)
        current_count = 0

max_count = max(max_count, current_count)
print(max_count)