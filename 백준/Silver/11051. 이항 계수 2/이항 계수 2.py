from math import comb
import sys
n,k = map(int,sys.stdin.readline().split())
print(comb(n,k)%10007)