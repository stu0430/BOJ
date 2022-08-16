import sys
n = int(input())
lst = []
for i in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)
lst = list(set(lst))
lst.sort(reverse=True)
for j in lst:
    print(j, sep='\n')