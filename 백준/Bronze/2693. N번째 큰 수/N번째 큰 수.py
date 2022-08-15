import sys
t = int(sys.stdin.readline())
for i in range(t):
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    print(a[-3])