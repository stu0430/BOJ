n, m = map(int, input().split())
lsn = []
see = []
for i in range(n):
    no_lsn = input()
    lsn.append(no_lsn)
for j in range(m):
    no_see = input()
    see.append(no_see)
lsn = set(lsn)
see = set(see)
no_lsn_see = list(lsn & see)
no_lsn_see.sort()
print(len(no_lsn_see))
for k in no_lsn_see:
    print(k)