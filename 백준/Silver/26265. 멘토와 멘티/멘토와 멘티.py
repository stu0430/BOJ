import sys

input = sys.stdin.readline

n = int(input())

array = [input().rstrip().split() for i in range(n)]

array.sort(key=lambda x: x[1], reverse=True)
array.sort(key=lambda x: x[0])

for i in array:
    print(*i)