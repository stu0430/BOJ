n, m  = map(int, input().split())

d = dict(zip(range(1, n + 1), [0] * n))

for _ in range(m):
    a, b = map(int, input().split())

    d[a] += 1
    d[b] += 1

for k, v in sorted(d.items(), key=lambda x: x[0]):
    print(v)