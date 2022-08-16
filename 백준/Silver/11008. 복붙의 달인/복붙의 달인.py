import sys
t = int(sys.stdin.readline())
for i in range(t):
    s,p = map(str,sys.stdin.readline().rstrip().split())
    x = s.count(p)
    s = s.replace(p,'')
    print(len(s)+x)