import sys

input = sys.stdin.readline

x = int(input())

stick = 64

count = 0

while x > 0:
    if x >= stick:
        x -= stick
        count += 1
    else:
        stick //= 2
        
print(count)