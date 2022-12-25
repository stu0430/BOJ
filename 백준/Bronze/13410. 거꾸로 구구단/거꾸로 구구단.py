import sys

input = sys.stdin.readline

n, k  = map(int, input().split())

array = [int(str(i * n)[::-1]) for i in range(1, k + 1)]

print(max(array))