n, m = map(int, input().split())

for i in range(n):
    print(' '.join(str((i * m) + j + 1) for j in range(m)))