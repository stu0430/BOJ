import sys

input = sys.stdin.readline

n = int(input())
v = list(map(int,input().split()))

s = sum(v)
array = [s - v[i] for i in range(n)]    
print(min(array))