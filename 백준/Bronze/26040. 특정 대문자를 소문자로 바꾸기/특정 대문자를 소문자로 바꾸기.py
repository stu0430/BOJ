import sys

input = sys.stdin.readline

a = input().rstrip()
b = set(input().rstrip().split())
c = ''

for i in a:
    if i in b:
        c += i.lower()
    else:
        c += i
        
print(c)