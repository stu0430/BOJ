import sys

input = sys.stdin.readline

k = int(input())

print('1' * k + '0' * (k - 1))