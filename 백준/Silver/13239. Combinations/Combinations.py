from math import comb
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    print(comb(n,k)%1000000007)