import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array1 = [list(map(int, input().split())) for i in range(n)]
array2 = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        print(array1[i][j] + array2[i][j], end = ' ')
    print()