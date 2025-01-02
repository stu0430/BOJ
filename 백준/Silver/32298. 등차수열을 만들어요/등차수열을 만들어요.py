n, m = map(int, input().split())

print(' '.join([str(m * (i + 2)) for i in range(n)]))