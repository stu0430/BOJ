import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    n = 0
    d = y - x

    while True:
        if d <= n * (n + 1):
            break
        n += 1
  
    if d <= n**2:
        print((n * 2) - 1)
 
    else:
        print(n * 2)