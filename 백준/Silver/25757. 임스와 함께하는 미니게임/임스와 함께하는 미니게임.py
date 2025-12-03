n, g = input().split()
n = int(n)

p = {input() for _ in range(n)}

if g == 'Y':
    print(len(p))
elif g == 'F':
    print(len(p) // 2)
elif g == 'O':
    print(len(p) // 3)