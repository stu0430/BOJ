import sys

input = sys.stdin.readline

n = int(input())

array = [int(input()) for i in range(n)]

print(sum(array) - n + 1)