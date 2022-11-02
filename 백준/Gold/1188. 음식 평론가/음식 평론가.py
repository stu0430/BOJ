import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(m - gcd(n, m))