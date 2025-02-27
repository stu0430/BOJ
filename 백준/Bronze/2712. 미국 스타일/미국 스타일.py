t = int(input())

for _ in range(t):
    n, m = input().split()
    n = float(n)

    if m == 'kg':
        print(f'{n * 2.2046:0.4f} lb')
        
    elif m == 'lb':
        print(f'{n * 0.4536:0.4f} kg')
        
    elif m == 'l':
        print(f'{n * 0.2642:0.4f} g')
        
    else:
        print(f'{n * 3.7854:0.4f} l')