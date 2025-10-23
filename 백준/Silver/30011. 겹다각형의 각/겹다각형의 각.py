n = int(input())
a = list(map(int, input().split()))

result = 180 * (a[0] - 2)

for i in range(1, n):
    result += 180 * a[i]
    
print(result)