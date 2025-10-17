while True:
    a, b, c, d = map(int, input().split())
    
    if a == 0:
        break
    
    cnt = 0
    while not (a == b == c == d):
        i = a
        a = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - i)
        cnt += 1
    
    print(cnt)