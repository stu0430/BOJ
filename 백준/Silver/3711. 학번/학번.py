n = int(input())

for _ in range(n):
    g = int(input())
    code = [int(input()) for i in range(g)]
    
    result = 0
    
    while True:
        result += 1
        if len({i % result for i in code}) == g:
            print(result)
            break