import sys
while True:
    lst = []
    code = sys.stdin.readline().rstrip()
    if code == 'END':
        break
    else:
        for i in code:
            lst.append(i)
        lst = lst[::-1]
        for j in lst:
            print(j, end='')
        print()