import sys

input = sys.stdin.readline

n = int(input())

result = 0

for i in range(1, n + 1):
    temp = i
    flag = True
    
    while temp > 0:
        if temp % 10 not in {4, 7}:
            flag = False
            break
            
        temp //= 10
        
    if flag:
        result = i
        
print(result)