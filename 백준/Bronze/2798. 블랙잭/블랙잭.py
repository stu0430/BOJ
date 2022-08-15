lst =[]
n,m = map(int, input().split())
a = list(map(int, input().split()))
if n == len(a):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                if a[i]+a[j]+a[k] <= m:
                    lst.append(a[i]+a[j]+a[k])
    print(max(lst))