import sys

input = sys.stdin.readline

s = int(input())
j = int(input())
h = int(input())
k = int(input())
c = int(input())

print(min(s, j, h) + min(k, c) - 50)