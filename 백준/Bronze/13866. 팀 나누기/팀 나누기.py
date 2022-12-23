import sys

input = sys.stdin.readline

array = list(map(int, input().split()))

a, b = max(array), min(array)

del array[array.index(a)]

del array[array.index(b)]

print(abs(sum(array) - (a + b)))