import sys

input = sys.stdin.readline

n, m = map(int, input().split())
v = list(map(int, input().split()))

total = sum(v)
supporters = 0

v.sort(reverse=True)

idx = 0
while total > supporters * 2:
    supporters += v[idx]
    idx += 1

print(m // (idx + 1))