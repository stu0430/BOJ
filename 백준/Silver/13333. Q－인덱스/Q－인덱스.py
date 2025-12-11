n = int(input())
array = list(map(int, input().split()))

array.sort()

for k in range(n, -1, -1):
    if k <= array[-k]:
        print(k)
        break