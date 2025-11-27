d1, d2, d3 = map(int, input().split())

a = (d1 + d2 + d3) / 2 - d3
b = (d1 + d2 + d3) / 2 - d2
c = (d1 + d2 + d3) / 2 - d1

if a <= 0 or b <= 0 or c <= 0:
    print(-1)
else:
    print(1)
    print(a, b, c)