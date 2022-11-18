import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(1, n):
        array[i][j] += array[i][j - 1]
        
for i in range(1, n):
    for j in range(n):
        array[i][j] += array[i - 1][j]
        
for i in range(m):  
    x1, y1, x2, y2 = map(int, input().split())
    
    if x1 == 1 and y1 == 1:
        print(array[x2 - 1][y2 - 1])
        
    elif x1 == 1:
        print(array[x2 - 1][y2 - 1] - array[x2 - 1][y1 - 2])
        
    elif y1 == 1:
        print(array[x2 - 1][y2 - 1] - array[x1 - 2][y2 - 1])
        
    else:
        print(array[x2 - 1][y2 - 1] - array[x1 - 2][y2 - 1] - array[x2 - 1][y1 - 2] + array[x1 - 2][y1 - 2])