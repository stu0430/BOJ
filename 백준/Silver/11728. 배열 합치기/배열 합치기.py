n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.extend(b)
a.sort()
for i in a:
    print(i, end=' ')