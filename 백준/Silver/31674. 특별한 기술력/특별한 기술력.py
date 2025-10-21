import sys

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

h.sort(reverse=True)

result = h[0]
for i in range(1, n):
    h[i] = h[i] + result
    result = (result + h[i]) % 1000000007

print(result)