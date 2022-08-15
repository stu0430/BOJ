n = int(input())
x = list(map(int, input().split()))
lst = []
for i in x:
    cnt = 0
    for j in range(i, 0, -1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        lst.append(i)
print(len(lst))