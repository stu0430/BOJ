import sys
from math import gcd

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(gcd(a, b))