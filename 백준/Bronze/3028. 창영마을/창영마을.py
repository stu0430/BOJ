import sys

input = sys.stdin.readline

s = input().rstrip()

array = [1, 0, 0]

for i in s:
    if i == 'A':
        array[0], array[1] = array[1], array[0]
    elif i == 'B':
        array[1], array[2] = array[2], array[1]
    elif i == 'C':
        array[0], array[2] = array[2], array[0]
        
for i in range(3):
    if array[i] == 1:
        print(i + 1)    