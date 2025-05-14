t = int(input())

for _ in range(t):
    r, c = map(int, input().split())
    
    if r != c:
        print('jinseo')
        print(min(r, c), min(r, c))
        
    else:
        print('dohoon')