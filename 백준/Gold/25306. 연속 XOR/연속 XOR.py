import sys

input = sys.stdin.readline

def xor(x):
    if x % 4 == 0:
        return x
    
    elif x % 4 == 1:
        return (x-1) ^ x
    
    elif x % 4 == 2:
        return (x-2) ^ (x-1) ^ x
    
    else:
        return 0

a, b = map(int, input().split())
    
print(xor(a - 1) ^ xor(b))