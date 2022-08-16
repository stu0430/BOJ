import sys
a,b,c = map(int, sys.stdin.readline().split())
lst = [a,b,c]
lst.sort()
print(lst[1])