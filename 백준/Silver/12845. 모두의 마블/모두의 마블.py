import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)
max_val = l[0]
result = sum(l[1:]) + max_val * (n - 1)

print(result)