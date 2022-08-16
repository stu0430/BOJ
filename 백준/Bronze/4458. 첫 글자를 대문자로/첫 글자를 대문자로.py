n = int(input())
for i in range(n):
    lst = []
    a = input()
    for j in a:
        lst.append(j)
    frst = lst[0]
    frst = frst.upper()
    del lst[0]
    lst.insert(0, frst)
    for k in lst:
        print(k, end='')
    print()