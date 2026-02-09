n = int(input())
a = sorted(list(map(int, input().split())))
flag = True

for i in range(n):
    if (i + 1) != a[i]:
        print(i + 1)
        flag = False
        break
    
if flag:
    print(n + 1)