import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    print(f'{i + 1}. {input().rstrip()}')