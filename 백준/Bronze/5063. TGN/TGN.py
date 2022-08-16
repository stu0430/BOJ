import sys
n = int(sys.stdin.readline())
for i in range(n):
    r,e,c = map(int, sys.stdin.readline().split())
    ad = e-r
    if ad > c:
        print('advertise')
    elif ad == c:
        print('does not matter')
    elif ad < c :
        print('do not advertise')