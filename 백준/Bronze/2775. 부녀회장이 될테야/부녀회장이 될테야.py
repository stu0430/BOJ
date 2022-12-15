import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    
    array = [[0] * (n + 1) for i in range(k + 1)]
    
    for i in range(1, n + 1):
        array[0][i] = i
        
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            array[i][j] = array[i - 1][j] + array[i][j - 1]
            
    print(array[k][n])