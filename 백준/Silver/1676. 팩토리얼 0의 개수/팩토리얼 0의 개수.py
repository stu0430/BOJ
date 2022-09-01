import sys
from math import factorial

input = sys.stdin.readline

n =  int(input())

x = str(factorial(n))[::-1]

if '0' not in x:
    print(0)
    
else:
    for i in x:
        if i != '0':
            print(x.index(i))
            break