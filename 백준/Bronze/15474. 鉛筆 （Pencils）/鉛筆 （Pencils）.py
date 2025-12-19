n, a, b, c, d = map(int, input().split())

if n % a == 0:
    x = (n // a) * b
else:
    x = (n // a + 1) * b

if n % c == 0:
    y = (n // c) * d
else:
    y = (n // c + 1) * d

if x > y:
    print(y)
else:
    print(x)