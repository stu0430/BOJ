n, m = map(int, input().split())

print(' '.join([str(m * (i + 1)) for i in range(1, n + 1)]))