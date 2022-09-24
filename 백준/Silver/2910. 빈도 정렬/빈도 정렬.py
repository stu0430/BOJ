import sys

input = sys.stdin.readline

lst = []
dic = dict()

n,c = map(int, input().split())

lst.append(input().rstrip().split())

lst = lst[0]

for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
    
dic = sorted(dic.items(), key=lambda x : -x[1])

for i in range(len(dic)):
    print((dic[i][0] + ' ') * dic[i][1], end='')