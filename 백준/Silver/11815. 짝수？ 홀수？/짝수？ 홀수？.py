n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    if x[i] == (int(x[i] ** 0.5) ** 2):
        print(1, end = " ")
    else:
        print(0, end = " ")