n, l = map(int, input().split())

for length in range(l, 101):
    s = (n / length) - ((length + 1) / 2)
    
    if s == int(s):
        s = int(s)
        
        if s + 1 >= 0:
            print(*range(s + 1, s + length + 1))
            break
else:
    print(-1)