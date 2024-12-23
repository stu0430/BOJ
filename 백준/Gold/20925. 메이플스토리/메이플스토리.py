import sys

input = sys.stdin.readline

N, T = map(int, input().split())
C, E = [], []

for _ in range(N):
    c, e = map(int, input().split())
    
    C.append(c)
    E.append(e)
    
array = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (T + 1) for _ in range(N)]

for i in range(N):
    if C[i] > 0:
        dp[i][0] = -1000000000
    
result = -1
        
for i in range(1, T + 1):
    for j in range(N):
        dp[j][i] = dp[j][i - 1] + E[j]
        for k in range(N):
            if j != k and i - array[k][j] >= 0 and dp[k][i - array[k][j]] >= C[j]:
                dp[j][i] = max(dp[j][i], dp[k][i - array[k][j]]) 
        result = max(result, dp[j][i])
    
print(result)