from math import lcm
import sys
n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a,b))