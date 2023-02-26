import sys

input = sys.stdin.readline

array = list(map(int, input().split()))

array.sort()

i = array[2]

while True:
    count = 0
    
    for j in array:
        if i % j == 0:
            count += 1
            
    if count >= 3:
        print(i)
        break
        
    i += 1