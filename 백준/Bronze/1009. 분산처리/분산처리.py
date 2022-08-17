import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    b = (b % 4) + 4
    pc = a ** b % 10
    if pc == 0:
        print(10)
    else:
        print(pc)
