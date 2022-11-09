import sys
from collections import defaultdict

input = sys.stdin.readline

n, p, q = map(int, input().split())

d = defaultdict(int)

d[0] = 1

def solve(n):
    if d[n] != 0:
        return d[n]
    
    d[n] = solve(n//p) + solve(n//q)
    
    return d[n]

print(solve(n))