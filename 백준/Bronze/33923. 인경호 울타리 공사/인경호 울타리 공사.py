n, m = map(int, input().split())
    
if n == m:
    print(((n - 2) ** 2) + 1)
    
else:
    print((min(n, m) - 1) ** 2)