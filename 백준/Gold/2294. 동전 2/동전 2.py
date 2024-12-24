import sys

input = sys.stdin.readline

n, k = map(int, input().split())

array = [int(input()) for _ in range(n)]

dp = [10001] * (k + 1)

dp[0] = 0

for i in range(n):
    for j in range(array[i], k + 1):
        dp[j] = min(dp[j], dp[j - array[i]] + 1)

if dp[k] == 10001:
    print(-1)
    
else:
    print(dp[k])