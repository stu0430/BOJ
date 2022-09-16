import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    result = []
    
    n = int(input())
    
    first_key = list(map(str, input().rstrip().split()))
    second_key = list(map(str, input().rstrip().split()))
    password = list(map(str, input().rstrip().split()))
    
    for j in first_key:
        result.append(password[second_key.index(j)])
        
    print(*result)