import sys

input = sys.stdin.readline

n = int(input())

array = [input().rstrip().split() for i in range(n)]

for i in range(n):
    array[i][1] = int(array[i][1])
    array[i][2] = int(array[i][2])
    array[i][3] = int(array[i][3])
    
array = sorted(array, key = lambda x : (x[3], x[2], x[1]))

print(array[-1][0])
print(array[0][0])