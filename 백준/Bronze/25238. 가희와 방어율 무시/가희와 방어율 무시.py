a, b = map(int, input().split())
ignore = a*(b/100)
x = a - ignore
if x >= 100:
    print(0)
else:
    print(1)