import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic, dic2 = {}, {}
for _ in range(N):
    team = input().rstrip()
    mems = []
    for i in range(int(input())):
        name = input().rstrip()
        dic[name] = team
        mems.append(name)
    dic2[team] = mems
for _ in range(M):
    prom = input().rstrip()
    cat = int(input())
    if cat == 1:
        print(dic[prom])
    else:
        memb = dic2[prom]
        print('\n'.join(sorted(memb)))