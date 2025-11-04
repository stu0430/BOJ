import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dp = {}
dp[0] = 0
dp[1] = 1
dp[2] = 1

def f(i):
    if i not in dp:
        if i % 2 == 0:
            dp[i] = (f(i // 2) * (f(i // 2) + 2 * f(i // 2 - 1))) % 1000000007        
        else:
            dp[i] = (f(i // 2) ** 2 + f(i // 2 + 1) ** 2) % 1000000007
    
    return dp[i]

n = int(input())
print(f(n))