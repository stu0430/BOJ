import sys

input = sys.stdin.readline

t = int(input())
 
for _ in range(t):
    n = int(input())
    
    result = 0
    
    for i in range(2, n + 1):
        x = n
        
        while x:
            if x % i == 0:
                result += 1
                x //= i
            else:
                break
            
    print(result)