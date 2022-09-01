import sys

input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    x, y = map(int, input().split())
    lst.append((x,y))
    
lst.sort()

for j,k in lst:
    print(j, k)