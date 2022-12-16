import sys

input = sys.stdin.readline

array = [list(map(int, input().split())) for i in range(9)]

max_array = [max(i) for i in array]

result = max(max_array)

print(result)
print(max_array.index(result) + 1, array[max_array.index(result)].index(result) + 1)