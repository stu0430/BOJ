n = int(input())

if '7' not in str(n):
    if n % 7 == 0:
        print(1)
        
    else:
        print(0)

elif '7' in str(n):
    if n % 7 == 0:
        print(3)
        
    else:
        print(2)