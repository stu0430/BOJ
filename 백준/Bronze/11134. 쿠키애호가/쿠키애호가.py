t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    
    if n % c == 0:
        print(n // c)
        
    else:
        print(n // c + 1)