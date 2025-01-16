import sys

input = sys.stdin.readline

array = [0] * 1001
result, count = 0, 0

for _ in range(int(input())): 
    d, c = input().rstrip().split()
    c = int(c)
    
    if d == 'jinju': 
        result = c
        
    elif c > 1000: 
        count += 1
        
    else: 
        array[c] += 1

for i in range(result + 1, 1001): 
    count += array[i]
    
print(result)
print(count)