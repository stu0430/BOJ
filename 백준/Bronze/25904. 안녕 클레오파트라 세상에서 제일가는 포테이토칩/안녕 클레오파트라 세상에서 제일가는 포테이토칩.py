n, x = map(int, input().split())
t = list(map(int, input().split()))

loop = True

while loop:
    for i in range(1, n + 1):
        if t[i - 1] < x:
            print(i)
            loop = False
            break
        else:
            x += 1