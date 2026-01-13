import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = 1
    
    while n != 1:
        if result < n:
            result = n
        
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    
    print(result)