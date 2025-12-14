import sys

input = sys.stdin.readline

t = int(input())

fibo = [0, 1]

while fibo[-1] < 1000000000:
    fibo.append(fibo[-1] + fibo[-2])

for _ in range(t):
    n = int(input())
    
    result = []
    count = len(fibo) - 1
    
    while n > 0:
        if n >= fibo[count]:
            n -= fibo[count]
            result.append(fibo[count])
            
        count -= 1
    
    result.sort()
    
    print(' '.join(map(str, result)))