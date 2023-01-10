import sys

input = sys.stdin.readline

n = int(input())
s = input().rstrip()

count = 0

for i in range(n):
    if s[i] == 'L':
        count += 1

if count == 0:
    print(n)
else:
    print(n - ((count // 2) - 1))