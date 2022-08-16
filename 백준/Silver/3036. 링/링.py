from math import gcd
import sys
input = sys.stdin.readline
n = int(input())
rings_r = list(map(int,input().split()))
for i in range(1,len(rings_r)):
    x = gcd(rings_r[0],rings_r[i])
    print(f'{rings_r[0]//x}/{rings_r[i]//x}')