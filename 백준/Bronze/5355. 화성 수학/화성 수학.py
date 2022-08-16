t = int(input())
for i in range(t):
    a = list(map(str, input().split()))
    a[0] = float(a[0])
    for j in a:
        if j == '@':
            a[0] *= 3
        elif j == '%':
            a[0] += 5
        elif j == '#':
            a[0] -= 7
    print('{0:.2f}'.format(a[0]))