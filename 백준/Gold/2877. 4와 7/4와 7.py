import sys

input = sys.stdin.readline

k = int(input())

s = bin(k + 1)[3:]

print(s.replace('0', '4').replace('1', '7'))