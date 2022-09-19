import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    
    if str(n**2)[len(str(n**2)) - len(str(n)):len(str(n**2))] == str(n):
        print('YES')
    else:
        print('NO')