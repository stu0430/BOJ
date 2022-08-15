import sys
n = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in B:
    if i in A:
        print(1, end='\n')
    else:
        print(0, end='\n')