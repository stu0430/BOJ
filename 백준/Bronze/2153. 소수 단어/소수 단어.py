def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

s = input()
result = 0  

for i in s:
    if 'a' <= i <= 'z':
        result += ord(i) - 96
        
    else:
        result += ord(i) - 38

if is_prime(result):
    print('It is a prime word.')
    
else:
    print('It is not a prime word.')