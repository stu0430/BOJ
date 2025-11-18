n = int(input())

count = 0
while n % 5 != 0:
    n -= 2
    count += 1
    if n < 0:
        count = -1
        break

if n >= 0:
    count += (n // 5)

print(count)