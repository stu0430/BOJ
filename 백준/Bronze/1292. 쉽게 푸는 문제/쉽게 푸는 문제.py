X = []
a, b = map(int, input().split())
if a == 1 and b == 1:
    print(1)
else:
    for i in range(b):
        if i == 0:
            pass
        else:
            for j in range(i):
                X.append(i)
    print(sum(X[a-1:b]))