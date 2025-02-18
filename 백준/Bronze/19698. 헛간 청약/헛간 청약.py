n, w, h, l = map(int, input().split())

result = (w // l) * (h // l)

if n < result:
    print(n)
else:
    print(result)