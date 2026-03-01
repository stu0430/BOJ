import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [-1] * (n + 1)

for i in range(n - 1, -2, -1):
    if i == n - 1:
        dp[i + 1] = 1
        
    else:
        result = 1
        for j in range(i + 1, n):
            if i == -1 or array[i] < array[j]:
                result = max(result, dp[j + 1] + 1)
                
        dp[i + 1] = result

print(dp[0] - 1)