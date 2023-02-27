import sys

input = sys.stdin.readline

n = int(input())

array = [int(input()) for i in range(n)]

if array[1] - array[0] == array[2] - array[1]:
    print(array[-1] + array[1] - array[0])
    
else:
    print(array[-1] * array[1] // array[0])