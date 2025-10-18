r, g, b = map(int, input().split())
count = 0

count += r // 3 + g // 3 + b // 3
r, g, b = r % 3, g % 3, b % 3

while r and g and b:
    count += 1
    r -= 1
    g -= 1
    b -= 1

while r and g:
    count += 1
    r -= 1
    g -= 1

while r and b:
    count += 1
    r -= 1
    b -= 1

while g and b:
    count += 1
    g -= 1
    b -= 1

if r > 0:
    count += 1
elif g > 0:
    count += 1
elif b > 0:
    count += 1

print(count)