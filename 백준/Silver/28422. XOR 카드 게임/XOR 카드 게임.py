import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [-1] * (n + 1)
dp[0] = 0

if n >= 2:
    dp[2] = (a[0] ^ a[1]).bit_count()
    
if n >= 3:
    dp[3] = (a[0] ^ a[1] ^ a[2]).bit_count()

for i in range(4, n + 1):
    take2 = dp[i-2] + (a[i-2] ^ a[i-1]).bit_count() if dp[i-2] >= 0 else -1
    take3 = dp[i-3] + (a[i-3] ^ a[i-2] ^ a[i-1]).bit_count() if dp[i-3] >= 0 else -1
    dp[i] = max(take2, take3)

if n == 1:
    print(0)
else:
    print(max(dp[n], 0))