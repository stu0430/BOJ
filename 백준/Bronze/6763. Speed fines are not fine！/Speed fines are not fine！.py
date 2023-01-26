import sys

input = sys.stdin.readline

a = int(input())
b = int(input())

c = b - a 

if c <= 0:
    print('Congratulations, you are within the speed limit!')
    exit()

if 1 <= c <= 20:
    f = 100
    
elif 21 <= c <= 30:
    f = 270
    
elif 31 <= c:
    f = 500
    
print(f'You are speeding and your fine is ${f}.')