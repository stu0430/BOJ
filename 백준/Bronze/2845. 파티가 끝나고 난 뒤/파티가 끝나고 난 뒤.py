l, p = map(int, input().split())

array = list(map(int, input().split()))

for i in array:
    print(i - l * p, end = ' ')