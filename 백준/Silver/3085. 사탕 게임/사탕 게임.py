import sys

input = sys.stdin.readline

n = int(input())

array = [list(input().rstrip()) for i in range(n)]

result = 0

def check(array):
    result = 0
    
    for i in range(n):
        count = 1
        
        for j in range(1, n):
            if array[i][j] == array[i][j - 1]:
                count += 1
            else:
                count = 1
                
            result = max(result, count)
            
        count = 1
        
        for j in range(1, n):
            if array[j][i] == array[j - 1][i]:
                count += 1
            else:
                count = 1
                
            result = max(result, count)
            
    return result

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
            result = max(result, check(array))
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
            
        if i + 1 < n:
            array[i][j], array[i + 1][j] = array[i + 1][j], array[i][j]
            result = max(result, check(array))
            array[i][j], array[i + 1][j] = array[i + 1][j], array[i][j]
            
print(result)