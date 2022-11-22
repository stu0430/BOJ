import sys

input = sys.stdin.readline

n = int(input())

file = dict()

for i in range(n):
    name = list(input().rstrip().split('.'))   
    if name[1] in file:   
        file[name[1]] += 1
    else:                      
        file[name[1]] = 1

file = sorted(file.items())

for key, value in file:
    print(key, value)