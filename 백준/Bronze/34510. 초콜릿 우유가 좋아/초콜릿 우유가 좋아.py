h1, h2, h3 = map(int, input().split())
n = int(input())

if n % 2 == 0:
    print((h2 + 2 * h3) * (n // 2))
else:
    print((h2 + 2 * h3) * (n // 2) + (h1 + h2 + h3))