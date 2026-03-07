import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1

for i in [2 ** k for k in range(21)]:
    if i <= n:
        for j in range(i, n + 1):
            dp[j] += (dp[j - i]) % 1000000000

print(dp[n] % 1000000000)