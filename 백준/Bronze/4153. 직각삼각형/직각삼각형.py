while True:
    lst = []
    a,b,c = map(int, input().split())
    if a == b == c == 0:
        break
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst_max = max(lst)
    lst.remove(lst_max)
    if (lst[0]**2) + (lst[1]**2) == lst_max**2:
        print('right')
    else:
        print('wrong')