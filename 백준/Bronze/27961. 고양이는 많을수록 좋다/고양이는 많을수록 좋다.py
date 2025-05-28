n = int(input())

cat = 1
result = 1

if n == 0:
    print(0)
    
else:
    while cat < n:
        cat *= 2
        result += 1
        
    print(result)