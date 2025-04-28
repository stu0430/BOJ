n, m = map(int, input().split())
a = list(map(int, input().split()))
print('DIMI' if n + m <= sum(a) else 'OUT')