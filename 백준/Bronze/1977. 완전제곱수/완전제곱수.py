import sys

input = sys.stdin.readline

m = int(input())
n = int(input())

lst = [i*i for i in range(1,101) if m <= i*i <=n]

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst), min(lst), sep='\n')