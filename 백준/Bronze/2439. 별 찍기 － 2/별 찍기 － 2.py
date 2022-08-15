n = int(input())
for i in reversed(range(n)):
    for j in range(n):
        if i <= j:
            print('*', end='')
        elif i > j:
            print(' ', end='')
    print()