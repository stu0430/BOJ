import sys
a,b = map(int, sys.stdin.readline().split())
if b>10000000:
    b = 10000000
Fal = [i for i in range(a,b+1) if str(i) == str(i)[::-1]]
def check_prime(num): 
    for i in range(2,int(num**0.5)+1):
        if num%i == 0: 
            return False 
    return True
Fal = [i for i in Fal if check_prime(i)]
for i in Fal:
    print(i)
print(-1)