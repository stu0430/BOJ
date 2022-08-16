import sys
t = int(sys.stdin.readline())
for i in range(t):
    yangjojang = {}
    n = int(sys.stdin.readline())
    for j in range(n):
        s, l = map(str, sys.stdin.readline().split())
        l = int(l)
        yangjojang[s] = l
    print(max(yangjojang, key = yangjojang.get))