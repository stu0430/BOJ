import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, e = map(int, input().split())
    
    if s == e or abs(s - e) == n - 1:
        print(0)
        
    elif abs(s - e) == 1 or s in {1, n}:
        print(1)
        
    else:
        print(2)