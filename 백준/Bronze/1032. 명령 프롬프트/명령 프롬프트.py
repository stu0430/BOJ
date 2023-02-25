import sys

input = sys.stdin.readline

n = int(input())

array = [input().rstrip() for i in range(n)]

result = ''

for i in range(len(array[0])):
    temp = array[0][i]
    
    for j in range(1, n):
        if temp != array[j][i]:
            temp = '?'
            break
            
    result += temp

print(result)