count = 1

while True :
    n = int(input())
    
    if n == 0:
        break
    
    if n * 3 % 2 == 0:
        print(f'{count:d}. even {(3 * n // 2) * 3 // 9:d}')
        
    else:
        print(f'{count:d}. odd {((3 * n + 1) // 2) * 3 // 9:d}')
    
    count += 1