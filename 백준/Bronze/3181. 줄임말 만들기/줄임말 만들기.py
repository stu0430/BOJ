import sys

input = sys.stdin.readline

s = input().rstrip().split()

array = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

for i in range(len(s)):
    if i == 0 or s[i] not in array:
        print(s[i][0].upper(), end = '')