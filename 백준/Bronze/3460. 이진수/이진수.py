import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    result = []
    
    for i in range(20):
        if n % 2 == 1:
            result.append(i)
            
        n //= 2
        
    print(*result)