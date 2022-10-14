import sys

input = sys.stdin.readline

n = input()

if '0' not in n:
    print(-1)

else:
    n = list(n)
    n.sort(reverse=True)
    n = int(''.join(n))
    
    if n % 30 == 0:
        print(n)
    else:
        print(-1)