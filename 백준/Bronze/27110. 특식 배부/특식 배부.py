import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

for i in range(len(array)):
    if array[i] > n:
        array[i] = n

print(sum(array))