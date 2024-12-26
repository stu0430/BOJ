import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    result = 0
    
    for i in range(1, 15):
        result += n // (5 ** i)
        
    print(result)