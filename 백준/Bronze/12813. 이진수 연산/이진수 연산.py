import sys

input = sys.stdin.readline

a = list(map(int, input().rstrip()))
b = list(map(int, input().rstrip()))

for i in range(5):
    for j in range(len(a)):
        if i == 0:
            print(a[j] & b[j], end = '')
            
        elif i == 1:
            print(a[j] | b[j], end = '')
            
        elif i == 2:
            print(a[j] ^ b[j], end = '')
            
        elif i == 3:
            print((a[j] + 1) % 2, end = '')
            
        else:
            print((b[j] + 1) % 2, end = '')
            
    print()