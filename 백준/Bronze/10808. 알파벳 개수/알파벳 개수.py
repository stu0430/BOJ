import sys

input = sys.stdin.readline

s = input().rstrip()

for i in range(97, 123):
    print(s.count(chr(i)), end=' ')