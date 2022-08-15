import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
pn = [True for i in range(m+1)]
pn[0] = False
pn[1] = False
p = 2
while (p**2 <= m):
    if (pn[p]):
        for i in range(p**2, m+1, p):
            pn[i] = False
    p += 1         
for i in range(n, m+1):
    if (pn[i]):
        print(i)