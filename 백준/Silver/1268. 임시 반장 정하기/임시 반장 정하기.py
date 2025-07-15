n = int(input()) 

array = [list(map(int, input().split())) for _ in range(n)]

d = [0] * n

for i in range(n):
    for j in range(i + 1, n):
        for grade in range(5):
            if array[i][grade] == array[j][grade]:
                d[i] += 1
                d[j] += 1
                break

result = d.index(max(d)) + 1

print(result)