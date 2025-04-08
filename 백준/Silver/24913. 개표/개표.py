import sys

input = sys.stdin.readline

n, q = map(int, input().split())

dp = [0] * 100001

sum_val = 0
temp = 0
max_val = 0

for _ in range(q):
    a, b, c = map(int, input().split())
    
    if a == 1:
        if c != n + 1:
            sum_val += b
            dp[c] += b
            max_val = max(max_val, dp[c])
        else:
            temp += b
    else:
        if max_val < temp + b and c <= ((temp + b - 1) * n - sum_val):
            print('YES')
            
        else:
            print('NO')