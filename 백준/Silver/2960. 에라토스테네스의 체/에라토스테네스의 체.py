n, k  = map(int, input().split())
lst = []
eratos = []
for i in range(2, n+1):
    lst.append(i)
while True:
    p = min(lst)
    lst.remove(p)
    eratos.append(p)
    for j in lst:
        if j%p == 0:
            lst.remove(j)
            eratos.append(j)
        else:
            pass
    if lst == []:
        break
print(eratos[k-1])