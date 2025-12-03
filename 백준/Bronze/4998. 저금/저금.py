try:
    while True:
        n, b, m = map(float, input().split())
        result = 0
        
        while (n < m):
            n += n * (b / 100)
            result += 1

        print(result)
        
except:
    exit()