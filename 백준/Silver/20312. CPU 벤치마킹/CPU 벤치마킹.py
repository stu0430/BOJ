import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

result = 0
Sum = 0

for i in range(n - 1):
    Sum += 1
    Sum *= m[i]
    Sum %= 1000000007
    
    result += Sum
    result %= 1000000007

print(result)