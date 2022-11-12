n, m = map(int, input().split())

a = [list(map(int, input())) for i in range(n)]
b = [list(map(int, input())) for i in range(n)]

def change(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]
            
count = 0

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            change(i, j)
            count += 1
            
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            exit()
            
print(count)