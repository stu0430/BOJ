import sys
n, m = map(int, sys.stdin.readline().split())
lst = []
lst_2 = []
cnt = 0
for i in range(n):
    a = sys.stdin.readline().strip()
    lst.append(a)
lst = set(lst)
for j in range(m):
    b = sys.stdin.readline().strip()
    lst_2.append(b)
for k in lst_2:
    if k in lst:
        cnt += 1
print(cnt)