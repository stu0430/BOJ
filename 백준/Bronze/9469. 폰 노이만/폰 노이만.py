p = int(input())

for _ in range(p):
    n, d, a, b, f = map(float, input().split())
    t = d / (a + b) * f
    print(f'{n} {t:6f}')