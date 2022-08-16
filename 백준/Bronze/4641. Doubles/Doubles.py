while True :
    lst = list(map(int, input().split()))
    count = 0
    if lst[0] == -1:
        break
    for i in range(len(lst)-1):
        if lst[i] * 2 in lst:
            count += 1
    print(count)