import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n
coin_count = 0

for i in range(n):
    coin = int(input())
    coins[i] += coin
    
coins.sort(reverse=True)

for j in coins:
    if k == 0:
        break
    else:
        if k % j != k:
            coin_count += k // j
            k %= j
        else:
            k %= j
            
print(coin_count)