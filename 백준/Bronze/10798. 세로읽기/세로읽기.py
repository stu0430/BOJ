import sys

input = sys.stdin.readline

array = [list(input().rstrip()) for _ in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(array[j]):
            print(array[j][i], end = '')