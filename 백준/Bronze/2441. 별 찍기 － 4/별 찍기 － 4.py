n = int(input())
for i in range(n):
    for j in range(n):
        if j >= i:
            print('*', end= '')
        elif i > j:
            print(' ', end='')
    print()