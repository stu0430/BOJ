import sys

input = sys.stdin.readline

n, m = map(int, input().split())

print('Yes' if n * 100 >= m else 'No')