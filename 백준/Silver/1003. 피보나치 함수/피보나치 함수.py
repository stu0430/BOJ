import sys

input = sys.stdin.readline

def fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while n:
            a,b = b, a+b
            n -= 1
        return a

t = int(input())

for i in range(t):
    n = int(input())
    if n == 0:
        print(1, 0)
    else:
        print(fibonacci(n-1), fibonacci(n))