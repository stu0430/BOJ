n = int(input())
x = 2
while n != 1:
    if n%x != 0:
        x += 1
    else:
        print(x)
        n = n//x