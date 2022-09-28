import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    
    array = []
    result = 1
    
    for j in range(n):
        a, b = map(str, input().rstrip().split())
        array.append(b)
        
    for k in set(array):
        result *= (array.count(k) + 1)
        
    print(result - 1)