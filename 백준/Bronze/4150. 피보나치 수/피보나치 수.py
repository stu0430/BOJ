n = int(input())

d = [0] * (n + 1)
d[0], d[1] = 1, 1

if n <= 1:
    print(1)
    
else:
    for i in range(1, n + 1):
        d[i] = d[i - 1] + d[i - 2]
        
    print(d[n - 1])