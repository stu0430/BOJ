import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
lst = [0,A[0]]
for e in range(1,len(A)):
    lst.append(lst[e]+A[e])
for k in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(lst[j]-lst[i-1])