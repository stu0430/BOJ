import sys
n = int(sys.stdin.readline())
for i in reversed(range(n)):
    for j in range(n):
        if i >= j:
            print('*', end='')
    print()