import sys

input = sys.stdin.readline

n = int(input())
s = input().rstrip()

num_r = s.count('R')
num_b = s.count('B')

r_left = len(s) - len(s.lstrip('R'))
r_right = len(s) - len(s.rstrip('R'))
b_left = len(s) - len(s.lstrip('B'))
b_right = len(s) - len(s.rstrip('B'))

print(min(num_r - r_left, num_r - r_right, num_b - b_left, num_b - b_right))