import sys

input = sys.stdin.readline

array = [int(input()) for i in range(9)]

array.sort()

for i in range(9):
    for j in range(i + 1, 9):
        if sum(array) - array[i] - array[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                    
                print(array[k])
                
            exit()