import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    query = input().split()
    l, r = map(int, query[1:3])

    if query[0] == '1':
        k = int(query[-1])
        cnt = a[l-1:r].count(k)
        print(cnt)

    elif query[0] == '2':
        a[l-1:r] = [0] * (r - l + 1)