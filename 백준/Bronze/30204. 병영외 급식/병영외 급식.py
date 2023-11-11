import sys

input =  sys.stdin.readline

n, x = map(int, input().split())
p = list(map(int, input().split()))

print(1 if sum(p) % x == 0 else 0)