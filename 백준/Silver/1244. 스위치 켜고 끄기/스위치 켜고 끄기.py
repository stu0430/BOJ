import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

s = int(input())

for i in range(s):
    g, x = map(int, input().split())

    if g == 1:
        for j in range(x - 1, n, x):
            array[j] = 1 - array[j]
            
    else:
        array[x - 1] = 1 - array[x - 1]
        
        for j in range(1, n):
            if x - 1 - j < 0 or x - 1 + j >= n:
                break
                
            if array[x - 1 - j] == array[x - 1 + j]:
                array[x - 1 - j] = 1 - array[x - 1 - j]
                array[x - 1 + j] = 1 - array[x - 1 + j]
                
            else:
                break
            
for i in range(n):
    print(array[i], end = ' ')
    
    if i % 20 == 19:
        print()