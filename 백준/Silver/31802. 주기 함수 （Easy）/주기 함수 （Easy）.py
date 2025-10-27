import sys

input = sys.stdin.readline

p = int(input())
integral = list(map(int, input().split()))
a, b = map(int, input().split())

a_q, a_r = divmod(a, p)
b_q, b_r = divmod(b, p)

if a_q == b_q:
    result = sum(integral[a_r:b_r])
else:
    result = sum(integral[a_r:])  + sum(integral[:b_r])  + sum(integral) * (b_q - a_q - 1)

print(result)