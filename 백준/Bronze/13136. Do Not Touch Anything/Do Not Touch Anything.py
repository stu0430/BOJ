r, c, n = map(int, input().split())

row = r // n

if r % n != 0:
    row += 1

col = c // n
if c % n != 0:
    col += 1

print(row * col)