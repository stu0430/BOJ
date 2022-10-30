import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def count(n, k):
    result = 0
    while n != 0:
        n //= k
        result += n
    return result

print(min(count(n, 2) - count(m, 2) - count(n - m, 2), count(n, 5) - count(m, 5) - count(n - m, 5)))