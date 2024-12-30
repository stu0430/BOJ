import sys

input = sys.stdin.readline

n = int(input())

counter, i = 1, 2

while i ** 2 <= n:
    if n % i == 0:
        counter = n // i
        break
    i += 1
    
print(n - counter)