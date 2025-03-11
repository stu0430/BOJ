def isPrime(num) :
    if num == 2 : return True
    else :
        for i in range(2, int(num**(1/2))+1) :
            if num % i == 0 : 
                return False
        return True
    
prime_num = []
for i in range(2, (123456*2)+1) :
    if isPrime(i) :
        prime_num.append(i)

while True :
    a = int(input())
    count = 0
    if a == 0 : 
        break
    else :
        for i in prime_num :
            if a < i <= 2*a :
                count += 1
        print(count)