import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
y = sorted(set(x))

dic = {y[i] : i for i in range(len(y))}

for i in x:
    print(dic[i], end = ' ')