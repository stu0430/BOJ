import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

array2 = sorted(array)

for i in array:
    print(array2.index(i), end = ' ')
    
    array2[array2.index(i)] = -1