import sys
n = int(sys.stdin.readline())
prime_1 = 0
for i in range(n):
    c, k = map(int, sys.stdin.readline().split())
    prime_1 += c*k
print(prime_1)