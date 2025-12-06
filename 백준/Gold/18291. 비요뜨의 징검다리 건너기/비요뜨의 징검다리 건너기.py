import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    
    if n == 1:
        print(1)
        
    else:
        a = 2
        b = n - 2
        result = 1
        
        while b > 0:
            if b % 2 != 0:
                result = (result * a) % 1000000007
                
            b //= 2
            a = (a * a) % 1000000007
            
        print(result)