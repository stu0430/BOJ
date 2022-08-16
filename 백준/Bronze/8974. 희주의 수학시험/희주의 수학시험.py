import sys
num = [i for i in range(1,46) for j in range(1,i+1)]
a, b = map(int, sys.stdin.readline().split())
print(sum(num[a-1:b]))