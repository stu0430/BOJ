n, l = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

total = 0
p = 0

for i in range(n):
    total += (array[i][0] - p)
    p = array[i][0]
    
    if (total % (array[i][1] + array[i][2])) <= array[i][1]:
        total += abs((total % (array[i][1] + array[i][2])) - array[i][1])

total += l - array[-1][0]

print(total)