import sys

input = sys.stdin.readline

while True:
    n = input().rstrip()
    
    if n == '0':
        break
    
    while len(n) != 1:
        n = str(sum(map(int, n)))
        
    print(n)