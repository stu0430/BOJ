n = int(input())

count = 0
bottom = 1

while n >= bottom:
    n -= bottom
    count += 1
    bottom += 4 * count

print(count)