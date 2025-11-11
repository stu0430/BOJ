import sys

input = sys.stdin.readline

n = int(input())
min_dp = [0, 0, 0]
max_dp = [0, 0, 0]

for i in range(n):
    a, b, c = map(int, input().split())
    
    if i == 0:
        min_dp = [a, b, c]
        max_dp = [a, b, c]
        
    else:
        min_dp = [
            min(min_dp[0], min_dp[1]) + a,
            min(min_dp[0], min_dp[1], min_dp[2]) + b,
            min(min_dp[1], min_dp[2]) + c
        ]
        max_dp = [
            max(max_dp[0], max_dp[1]) + a,
            max(max_dp[0], max_dp[1], max_dp[2]) + b,
            max(max_dp[1], max_dp[2]) + c
        ]

print(max(max_dp), min(min_dp))