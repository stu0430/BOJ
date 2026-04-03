import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

inc = [1 for i in range(n)]
dec = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            inc[i] = max(inc[i], inc[j] + 1)
            
        if a[::-1][i] > a[::-1][j]:
            dec[i] = max(dec[i], dec[j] + 1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = inc[i] + dec[n - i - 1] - 1

print(max(result))