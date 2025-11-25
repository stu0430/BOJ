a, b, n, w = map(int, input().split())

count = 0
result = None
for i in range(1, n):
    j = n - i
    if j >= 1 and a * i + b * j == w:
        count += 1
        result = (i, j)
        if count > 1:
            break

if count == 1:
    print(result[0], result[1])
else:
    print(-1)