from math import comb
import sys
while True:
    n,k = map(int,sys.stdin.readline().split())
    if n == 0 and k == 0:
        break
    else:
        print(comb(n,k))