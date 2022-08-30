import sys

input = sys.stdin.readline

def prime_check(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

lst = set([i for i in range(2,10001) if prime_check(i)])

t = int(input())

for i in range(t):
    n = int(input())
    x = n // 2
    y = x
    while n // 2 > 0:
        if x in lst and y in lst:
            print (x, y)
            break
        else:
            x -= 1
            y += 1