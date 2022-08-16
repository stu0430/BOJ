import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
a.sort()
for i in a:
    print(i, end = ' ')