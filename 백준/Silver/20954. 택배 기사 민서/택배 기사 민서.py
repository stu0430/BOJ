import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x = int(input())
    
    count = 0
    i = 1
    
    while True:
        if 0 <= x <= i:
            count += i // 2 + x
            break
        count += i // 2 + i
        
        if -i <= x <= 0:
            count += i + (-x)
            break
        count += i + i
        
        i *= 2
    
    print(count)