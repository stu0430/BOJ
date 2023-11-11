import sys
from math import factorial

input = sys.stdin.readline

e = 0

print('n e')
print('- -----------')

for n in range(10):
    e += 1 / factorial(n)

    if n == 0 or n == 1:
        print(f'{n} {e:.0f}')
    
    elif n == 2:
        print(f'{n} {e:.1f}')

    else:
        print(f'{n} {e:.9f}')