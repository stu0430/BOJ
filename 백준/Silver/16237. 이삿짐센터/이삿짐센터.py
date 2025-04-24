a, b, c, d, e = map(int, input().split())
count = e + d + c

a = max(0, a - d)

if b >= c:
    b -= c
    count += b // 2 + b % 2
    a -= b // 2
    
    if b % 2:
        a -= 3
else:
    c -= b
    a -= c * 2

if a > 0:
    count += a // 5
    
    if a % 5:
        count += 1

print(count)