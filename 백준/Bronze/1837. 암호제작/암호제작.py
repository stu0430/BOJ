import sys

input = sys.stdin.readline

p, k = map(int, input().split())

array = [True] * k

for i in range(2, k):
    if array[i]:
        j = 2
        
        while i * j < k:
            array[i * j] = False
            j += 1
            
for i in range(2, k):
    if array[i] and p % i == 0:
        print('BAD', i)
        break
    
else:
    print('GOOD')