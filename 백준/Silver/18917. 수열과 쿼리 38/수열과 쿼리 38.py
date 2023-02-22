import sys

input = sys.stdin.readline

m = int(input())

sum = 0
xor = 0

for i in range(m):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        sum += query[1]
        xor ^= query[1]
        
    elif query[0] == 2:
        sum -= query[1]
        xor ^= query[1]
        
    elif query[0] == 3:
        print(sum)
        
    elif query[0] == 4:
        print(xor)