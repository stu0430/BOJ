import sys
input = sys.stdin.readline

while True:
    n = int(input())
    
    if n == 0:
        break
        
    array = [input().rstrip() for _ in range(n)]
    array.sort(key=lambda x: x.lower())
    
    print(array[0])