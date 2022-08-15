L = []
for i in range(9):
    a = int(input())
    L.append(a)
print(max(L))
print(L.index(max(L))+1)