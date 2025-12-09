def power(a, b, c):
    if b == 1:
        return a % c
    
    half = power(a, b // 2, c)
    result = (half * half) % c
    
    if b % 2 == 1:
        result = (result * a) % c
    
    return result

a, b, c = map(int, input().split())
print(power(a, b, c))