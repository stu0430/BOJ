import sys

input = sys.stdin.readline

n = int(input())
array = input().rstrip().split()
tier = ['B','S','G','P','D']

d, x = [0] * n, []

for i in range(n):
    d[i] = tier.index(array[i][0]) * 1000 + (1000 - int(array[i][1:]))
    
if d == sorted(d):
    print('OK')
    
else:
    print('KO')
    
    for i in range(n):
        if d[i] != sorted(d)[i]:
            x.append(array[i])
            
    print(' '.join(reversed(x)))