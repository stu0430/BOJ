import sys

input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    s = input().rstrip()
    temp = ''
    
    for char in s:
        if char.isdigit():
            temp += char
            
        elif len(temp):
            result.append(int(temp))
            temp = ''
            
    if temp:
        result.append(int(temp))

result = sorted(result, key=int)

print(*result, sep='\n')