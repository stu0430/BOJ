import sys

input = sys.stdin.readline

x = int(input())
y = int(input()) * 3
z = int(input())

print(f'The 1-3-sum is {x + y + z + 91}')