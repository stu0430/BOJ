import sys

input = sys.stdin.readline

n = int(input())
x = int((n * 0.15) + 0.5)
         
if n == 0:
    print(0)

else:
    o = sorted([int(input()) for i in range(n)])
    print(int((sum(o[x:n - x]) / (n - 2 * x)) + 0.5))