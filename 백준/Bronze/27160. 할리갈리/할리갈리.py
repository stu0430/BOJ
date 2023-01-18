import sys

input = sys.stdin.readline

n = int(input())

dic = {'STRAWBERRY' : 0, 'BANANA' : 0, 'LIME' : 0, 'PLUM' : 0}

for i in range(n):
    s, x = input().rstrip().split()
    dic[s] += int(x)
    
print('YES' if 5 in dic.values() else 'NO')