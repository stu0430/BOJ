import sys
import math
t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a,b), math.gcd(a,b))