fibo = [0] * 21

fibo[0] = 1
fibo[1] = 2

for i in range(2, 21):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

t = int(input())
for _ in range(t):
    result = 0
    
    x = int(input())
    
    for i in range(20, 0, -1):
        if x >= fibo[i]:
            x -= fibo[i]
            result += fibo[i - 1]
    
    print(result)