import sys

input = sys.stdin.readline

n = int(input())

array = [0] * 26
result = []

for i in range(n):
    l = input().rstrip()
    array[ord(l[0]) - 97] += 1

for i, n in enumerate(array):
    if n >= 5:
        result.append(chr(i + 97))

if result:
    print(*result, sep='')
else:
    print('PREDAJA')