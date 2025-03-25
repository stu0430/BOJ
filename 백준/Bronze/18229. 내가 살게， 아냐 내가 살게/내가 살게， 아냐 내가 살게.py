n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [0] * n

for i in range(m):
    for j in range(n):
        b[j] += a[j][i]
        
        if b[j] >= k:
            print(j + 1, i + 1)
            exit()