import sys

input = sys.stdin.readline

n = int(input())
criminal = ''

for _ in range(n):
    name = input().rstrip()

    if 'S' in name:
        criminal = name

print(criminal)