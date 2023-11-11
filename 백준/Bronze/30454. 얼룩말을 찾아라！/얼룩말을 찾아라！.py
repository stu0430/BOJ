import sys

input = sys.stdin.readline

n, l = map(int, input().split())

zebra = [input().rstrip() for _ in range(n)]

result = []

for i in zebra:
    cnt = 0
    for j in i.split('0'):
        if j != '':
            cnt += 1
    result.append(cnt)

b = max(result)

print(b, result.count(b))