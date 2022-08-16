import sys
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    else:
        lst = []
        for i in range(n-1,0,-1):
            if n % i == 0:
                lst.append(i)
        lst.sort()
        if sum(lst) == n:
            print(f'{n} = ', end = '')
            for j in range(len(lst)):
                if j == len(lst)-1:
                    print(str(lst[j]))
                else:
                    print(str(lst[j]), '+',end = ' ')
        else:
            print(f'{n} is NOT perfect.')