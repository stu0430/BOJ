t = int(input())
numbers = list(map(int, input().split()))

for n in numbers:
    c = 0
    
    for i in range(1, n):
        if n % i == 0:
            c += i
    
    if c > n:
        print('Abundant')
    elif c == n:
        print('Perfect')
    else:
        print('Deficient')