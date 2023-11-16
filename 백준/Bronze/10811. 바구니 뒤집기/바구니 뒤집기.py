import sys

input = sys.stdin.readline

n, m = map(int, input().split())

basket = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)