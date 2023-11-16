import sys

input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))

if n in c:
    print(c.count(n))
else:
    print(0)