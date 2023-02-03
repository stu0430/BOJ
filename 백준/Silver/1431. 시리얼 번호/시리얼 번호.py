import sys

input = sys.stdin.readline

n = int(input())

array = [input().rstrip() for i in range(n)]

array.sort()

array.sort(key = lambda x: (len(x), sum(map(int, filter(str.isdigit, x))), x))

for i in array:
    print(i)