import sys

input = sys.stdin.readline

l = int(input())
array = list(map(int, input().split()))
n = int(input())

array.append(0)
array.sort()

x, y = 0, 0

for i in range(len(array)):
    if n < array[i]:
        x = i - 1
        y = i
        break

    elif n == array[i]:
        print(0)
        exit()

print(((n - 1) - (array[x] + 1) + 1) * ((array[y] - 1) - n + 1) + ((array[y] - 1) - (n + 1) + 1))