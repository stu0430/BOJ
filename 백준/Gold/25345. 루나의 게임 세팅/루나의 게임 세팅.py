import sys

input = sys.stdin.readline

n, k = map(int, input().split())

result = 1
for i in range(k):
    result = result * (n - i) // (i + 1)
    
print((result * pow(2, k - 1, 1000000007)) % (1000000007))